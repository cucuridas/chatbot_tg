from core.config import Settings
from abstract.connAbstract import Connect
import redis


class RedisConnection(Connect):
    """
    레디스 connection을 만드는 클래스입니다
    """

    def getConenction(self):
        self.conn = redis.StrictRedis(host=Settings.REDIS_HOST, port=Settings.REDIS_PORT)
        return self.conn

    def checkConnection(self):
        if self.conn.ping():
            return True
        else:
            raise Exception("Redis connection fail")
