from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8080


appSettings = AppSettings()
