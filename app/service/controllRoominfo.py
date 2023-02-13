import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from datetime import timedelta
import json
from app.service.parsing import ParsingData
from app.service.redis import RedisClient

CONN = RedisClient(1)


class ControllRoominfo:
    def registRoominfo(result):
        key, value = ParsingData.prseWebhook(result)
        CONN.setContent(key, value, timedelta(minutes=3))
        # CONN.setContent(key, value)
        return "Success"

    def addServiceRoominfo(key, serviceInfo: dict):
        if serviceInfo == None:
            return "None value"
        else:
            value = CONN.getContent(key)
            value.update(serviceInfo)
            CONN.setContent(key, value, timedelta(minutes=3))
            return value

    def deleteRoominfo(key):
        CONN.delContent(key)
        return "Success"
