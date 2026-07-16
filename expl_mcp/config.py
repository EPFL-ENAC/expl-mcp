from functools import lru_cache

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MCP_API_KEY: str
    AREE_API_URL: str = "http://aree.epfl.ch/AREEService"
    AREE_API_USERNAME: str
    AREE_API_PASSWORD: str


@lru_cache()
def get_config():
    return Config()


config = get_config()
