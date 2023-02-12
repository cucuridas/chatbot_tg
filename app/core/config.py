import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # redis 관련 설정
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = os.getenv("REDIS_PORT")
    REDIS_DB: int = os.getenv("REDIS_DB", 0)
    # elasticsearch 관련 설정
    ELASTCSEARCH_HOST: str = os.getenv("ELASTCSEARCH_HOST")
    ELASTCSEARCH_PORT: int = os.getenv("ELASTCSEARCH_PORT", 9200)
    # webex 관련 설정
    WEBEX_API: str = "https://api.ciscospark.com/v1/"
    WEBEX_BOT_TOKEN: str = os.getenv("WEBEX_BOT_TOKEN")
    WEBEX_BOT_NAME: str = os.getenv("WEBEX_BOT_NAME")
    WEBEX_BOT_EMAIL: str = os.getenv("WEBEX_BOT_EMAIL")
    # webhook 관련 설정
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")
    WEBHOOK_NAME: str = os.getenv("WEBHOOK_NAME")
    # Database 정보
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWROD: str = os.getenv("DB_PASSWROD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
