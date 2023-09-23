from pydantic_settings import BaseSettings
from pydantic import root_validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    KEY: str
    ALGO: str

    @root_validator(skip_on_failure=True)
    def get_database_url(cls, v):
        v['DATABASE_URL'] = f'postgresql+asyncpg://' \
                            f'{v["POSTGRES_USER"]}:{v["POSTGRES_PASSWORD"]}@{v["DB_HOST"]}:{v["DB_PORT"]}/{v["POSTGRES_DB"]}'
        return v

    @root_validator(skip_on_failure=True)
    def get_key(cls, v):
        v['KEY'] = f'{v["KEY"]}'
        return v

    @root_validator(skip_on_failure=True)
    def get_algo(cls, v):
        v['ALGO'] = f'{v["ALGO"]}'
        return v

    class Config:
        env_file = '.env'


settings = Settings()



