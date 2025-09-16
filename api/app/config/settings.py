from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Stores type-validated reference to environment variables"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_ignore_empty=True,
    )

    APP_NAME: str = "flashcard-quiz"
    ENVIRONMENT: Literal["local", "production"] = "local"
    HOST: str
    PORT: int
