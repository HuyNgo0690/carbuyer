import os


class Config:
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'covid')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', "5432")
    APP_PORT = os.environ.get('APP_PORT', "5001")
    LOGGING_CONF = os.environ.get('LOGGING_CONF', "config/logging.conf")
    LOGGER = os.getenv("LOGGER", "commonLogger")
