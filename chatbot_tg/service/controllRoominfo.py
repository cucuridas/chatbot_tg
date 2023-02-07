from datetime import timedelta
import json
from service.parsing import ParsingData
from service.redis import RedisClient


class ControllRoominfo:
    def registRoominfo(result):
        conn = RedisClient(1)
        key, value = ParsingData.prseWebhook(result)
        conn.setContent(key, value, timedelta(minutes=3))
        return "Success"

    def updateRomminfo(key, serviceInfo: dict):
        conn = RedisClient(1)
        value = conn.getContent(key)
        value.update(serviceInfo)
        conn.setContent(key, value, timedelta(minutes=3))
        return "Success"
