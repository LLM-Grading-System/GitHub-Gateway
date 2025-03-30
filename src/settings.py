from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    GITHUB_APPS_PRIVATE_KEY_PATH: str = Field(default="")
    GITHUB_APPS_CLIENT_ID: str = Field(default="")
    GITHUB_PERSONAL_ACCESS_TOKEN: str = Field(default="")

    KAFKA_BOOTSTRAP_SERVERS: str = Field(default="localhost:29092")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


app_settings = AppSettings()
