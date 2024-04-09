import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    DISCORD_TOKEN: str = os.environ.get("DISCORD_TOKEN")
    CHANNEL_ID: int = os.environ.get("CHANNEL_ID")
    TEXTCHEST_TOKEN: str = os.environ.get("TEXTCHEST_TOKEN")
    # FLY_TOKEN: str = os.environ.get("FLY_TOKEN")

    ZR_KEY: str = os.environ.get("ZR_KEY")

    URL: str = os.environ.get("URL")

    LOG_OPTION: int = os.environ.get("LOG_OPTION")
    LOGGER_NAME: str = os.environ.get("LOGGER_NAME")

    DB_NAME: str = os.environ.get("POSTGRES_DB")
    DB_USER: str = os.environ.get("POSTGRES_USER")
    DB_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    DB_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_PORT: str = os.environ.get("POSTGRES_PORT")


settings = Settings()
