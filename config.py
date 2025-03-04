from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """read the settings from .env file"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    telegram_api_id: "22473416"
    telegram_api_hash: "ca4a166df6f575a22497adcc1451cef6"
    telegram_bot_token: "7562806732:AAHv28jjwECkKXFvCMUJv9Y68OnqVEar1wk"
    telegram_bot_token_2: str
    admins: list["@Adityamajumdaar"]
    limit_spam: int
    admin_to_update_of_payment: int


@lru_cache
def get_settings() -> Settings:
    """get the settings from .env file"""
    return Settings()
