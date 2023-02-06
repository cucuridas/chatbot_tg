from connection.redis import RedisConnection
import json


class RedisClient:
    def __init__(self) -> None:
        self.conn = RedisConnection().getConenction()

    def setContent(self, inputKey: str, inputValue: str) -> str:
        self.conn.set(inputKey, json.dumps(inputValue))

    def getContent(self, getKey: str) -> dict:
        result = self.conn.get(getKey)
        if type(result) != dict:
            return json.loads(result)
        else:
            return result
