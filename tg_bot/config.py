from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    MONGO_TOKEN: SecretStr

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

settings = Settings()