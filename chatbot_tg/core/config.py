import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ELASTCSEARCH_HOST: str = os.getenv("ELASTCSEARCH_HOST")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = os.getenv("REDIS_PORT")
    REDIS_DB: int = os.getenv("REDIS_DB", 0)
