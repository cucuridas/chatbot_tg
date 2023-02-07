from app.service.parsing import ParsingData
from app.connection.redis import RedisConnection
import json
from typing import Any
from datetime import timedelta


class RedisClient:
    def __init__(self, db=None) -> None:
        self.conn = RedisConnection().getConenction(db)

    def setContent(self, inputKey: str, inputValue: Any, expire=None) -> str:
        self.conn.set(inputKey, json.dumps(inputValue), ex=expire)

    def getContent(self, getKey: str) -> dict:
        result = self.conn.get(getKey)
        if result != None:
            return json.loads(result)
        else:
            return result

    def delContent(self, delKey: str):
        self.conn.delete(delKey)
