import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")

from app.connection.elasticsearch import ElasticsearchConnection
import logging


CONN = ElasticsearchConnection()
conn = CONN.getConenction()


def checkPut():
    pass


def checkSearch():
    pass


if __name__ == "__main__":
    CONN.checkConnection()
    # checkPut()
    # print(checkSearch())
