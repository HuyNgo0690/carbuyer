from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    CLIENT_ORIGIN: str
    APP_PORT: int
    DEBUG_PORT: int

    class Config:
        env_file = './app.env'


settings = Settings()
