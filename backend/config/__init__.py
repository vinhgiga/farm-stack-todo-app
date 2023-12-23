import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    # common settings
    DEBUG_MODE: bool = True
    RELOAD_MODE: bool = True
    # server settings
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    # database settings
    DB_URL: str = os.getenv("DB_URL", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "TODO")

settings = Settings()
