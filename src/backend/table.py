from enum import Enum

from sqlalchemy import Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserRole(str, Enum):
    ADMIN = "Admin"
    USER = "User"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(Text, unique=True, nullable=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped["UserRole"] = mapped_column(Text, nullable=False, default=UserRole.USER)









