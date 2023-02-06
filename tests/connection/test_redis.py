import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")

from chatbot_tg.connection.redis import RedisConnection
import logging


CONN = RedisConnection()
conn = CONN.getConenction()


def checkSet():
    conn.set("test_key", "test_value")
    logging.info("정상작동")
    return "Success"


def checkGet():
    return conn.get("test_key")


if __name__ == "__main__":
    CONN.checkConnection()
    checkSet()
    return_vlaue = checkGet()
    print(return_vlaue)
