

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "LegalEase"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.5-flash"
    backend_url: str = "http://127.0.0.1:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


def get_settings():
    return Settings()