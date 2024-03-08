import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent
print(BASE_DIR)


class AuthJWT(BaseSettings):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire: int = 1

class DatabaseSettings(BaseSettings):
    url: str = os.getenv("POSTGRES_URL")
    echo: bool = True


class AppSettings(BaseSettings):
    host: str = "localhost"
    port: int = 10000

    database: DatabaseSettings = DatabaseSettings()
    auth: AuthJWT = AuthJWT()


setting = AppSettings()
