from pydantic import BaseModel
from src.backend.table import UserRole


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class BaseUser(BaseModel):
    username: str
    email: str


class User(BaseUser):
    id: int
    role: UserRole

    class Config:
        from_attributes = True


class RegisterUser(BaseUser):
    password: str

