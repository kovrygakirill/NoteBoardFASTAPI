from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DB_URL: str
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    class Config:
        env_file = '.env'


settings = Settings()
