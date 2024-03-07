from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseSettings(BaseSettings):
    pass


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 10000


appSettings = AppSettings()
