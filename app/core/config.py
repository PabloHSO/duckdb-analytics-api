from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_PATH: str = "data/analytics.duckdb"

settings = Settings()
