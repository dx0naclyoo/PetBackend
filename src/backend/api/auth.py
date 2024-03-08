from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models import auth as model
from src.backend.services.auth import services
from src.backend.database import databaseHandler

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.get("/", response_model=model.User)
async def get_user(user: model.User = Depends(services.get_current_user)):
    return user


@router.post("/login", response_model=model.Token)
async def login(
        userdata: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(databaseHandler.get_session)
):
    return await services.login(username=userdata.username, password=userdata.password, session=session)


@router.post("/register", response_model=model.Token)
async def register(
        userdata: model.RegisterUser,
        database_session: AsyncSession = Depends(databaseHandler.get_session)):
    return await services.register(userdata, database_session)
