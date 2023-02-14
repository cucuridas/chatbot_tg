import sys
import asyncio


sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")

from app.connection.smtp import Smtp


if __name__ == "__main__":
    Smtp.getConnection()
