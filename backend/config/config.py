import os


class Config:
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'admin')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'cars')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', "5432")
    APP_PORT = os.environ.get('APP_PORT', "5001")
