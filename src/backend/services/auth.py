from datetime import datetime
from datetime import timedelta
from typing import Any

import bcrypt
import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.database import databaseHandler
from src.backend.models import auth as model
from src.backend.settings import setting
from src.backend import table

oauth_schema = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class AuthService:

    @classmethod
    def encode_jwt(
            cls,
            payload: dict,
            private_key: str = setting.auth.private_key_path.read_text(),
            algorithm: str = setting.auth.algorithm,
            expire_timedelta: timedelta | None = None,
            expire_minutes: int = setting.auth.access_token_expire,
    ):

        to_encode = payload.copy()
        now = datetime.utcnow()

        if expire_timedelta:
            expire = now + expire_timedelta
        else:
            expire = now + timedelta(minutes=expire_minutes)

        to_encode.update(
            exp=expire,
            iat=now,
        )

        return jwt.encode(to_encode, key=private_key, algorithm=algorithm)

    @classmethod
    def decode_jwt(
            cls,
            token: str | bytes,
            public_key: str = setting.auth.public_key_path.read_text(),
            algorithms: str = setting.auth.algorithm) -> dict:

        return jwt.decode(token, key=public_key, algorithms=[algorithms])

    @classmethod
    def hash_password(cls, password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    @classmethod
    def validate_password(cls, password: str, hash_password: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hash_password)

    async def validate_token(
            self,
            token,
    ) -> model.User:

        try:
            confirm_user = self.decode_jwt(token).get("user")

        except PyJWTError as ex:
            print(f"[INFO] Ошибка JWT Токена", ex)

        try:
            user = model.User.parse_obj(confirm_user)
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials") from None

        return user

    async def get_current_user(self, token: str = Depends(oauth_schema)) -> model.User:
        return await self.validate_token(token)

    def create_token(self, user: table.User) -> model.Token:
        userdata = model.User.parse_obj(user)

        payload = {
            "sub": str(userdata.id),
            "user": userdata.dict()
        }

        return model.Token(access_token=self.encode_jwt(payload))

    async def login(self, username, password, session: AsyncSession) -> model.Token:
        stmt = select(table.User).where(table.User.username == username)
        db_response = await session.execute(stmt)
        user = db_response.scalar()

        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User does not exist, please register")

        # hashed_password = str.encode(user.password, encoding="utf-8")

        if self.validate_password(password, str.encode(user.password, encoding="utf-8")):
            return self.create_token(user)

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")

    async def register(
            self,
            userdata: model.RegisterUser,
            session: AsyncSession
    ) -> model.Token:

        user = table.User(
            email=userdata.email,
            username=userdata.username,
            password=str(self.hash_password(userdata.password))
            .replace("b'", "").replace("'", "")
        )

        username_stmt = select(table.User).where(table.User.username == userdata.username)
        database_response = await session.execute(username_stmt)
        login_check = database_response.scalar()

        email_stmt = select(table.User).where(table.User.username == userdata.email)
        database_response_email = await session.execute(email_stmt)
        email_check = database_response_email.scalar()

        if login_check:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")

        if email_check:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists")

        session.add(user)
        await session.commit()

        return self.create_token(user)


services = AuthService()

