from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 10000


appSettings = AppSettings()
