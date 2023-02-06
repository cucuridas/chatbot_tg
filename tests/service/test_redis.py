import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from chatbot_tg.service.redis import RedisClient


if __name__ == "__main__":
    service = RedisClient()

    service.setContent("testValue", "test")
    result = service.getContent("testValue")
    print(result)
