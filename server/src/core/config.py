from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    DATABASE_URL: str ="sqlite+aiosqlite:///./database.sqlite3"
    JWT_ALG: str ='HS256'
    JWT_KEY: str ='JWT_KEY'

settings = Settings()
