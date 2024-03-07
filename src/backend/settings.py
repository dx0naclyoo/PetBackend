from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseSettings(BaseSettings):
    url: str = os.getenv("POSTGRES_URL")
    echo: bool = True


class AppSettings(BaseSettings):
    host: str = "localhost"
    port: int = 10000


app_settings = AppSettings()
database_settings = DatabaseSettings()
