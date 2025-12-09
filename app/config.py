from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_WEBHOOK_KEY: str
    POLYGON_API_KEY: str
    ALPACA_API_KEY: str
    ALPACA_SECRET: str
    RH_USERNAME: str
    RH_PASSWORD: str
    LOGGING_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
