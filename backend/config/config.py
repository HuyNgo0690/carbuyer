from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    APP_PORT: int
    DEBUG_PORT: int
    LOGGING_CONF: str
    LOGGER: str

    class Config:
        env_file = './app.env'


settings = Settings()
