from functools import lru_cache

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MCP_API_KEY: str


@lru_cache()
def get_config():
    return Config()


config = get_config()
