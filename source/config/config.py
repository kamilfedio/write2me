from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


env_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(env_path)

class Config(BaseSettings):
    title: str = 'write2me'
    description: str ='app dedicated to forms on the pages'
    version: str ='0.0.1'
    debug: bool = True
    DB_ADDRESS: str

    class Config:
        env_file = '.env'


class ConfigMiddleware(BaseSettings):
    allow_origins: list[str] = ['*']
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]