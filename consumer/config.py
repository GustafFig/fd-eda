from typing import Dict

from pydantic import Field, validator, config
from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import make_url


class Settings(BaseSettings):
    database_conn_str: str
    kafka_topic: str = "balances"
    kafka_bootstrap_server: str = "kafka:29092"

    class Config(config.BaseConfig):
        env_file = ".env"

settings = Settings()
