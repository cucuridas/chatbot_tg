from app.core.config import Settings
from app.abstract.connAbstract import Connect
import redis


class RedisConnection(Connect):
    """
    레디스 connection을 만드는 클래스입니다
    """

    def getConenction(self, db=None):
        self.conn = redis.StrictRedis(
            host=Settings.REDIS_HOST, port=Settings.REDIS_PORT, db=db or 0
        )
        return self.conn

    def checkConnection(self):
        if self.conn.ping():
            return True
        else:
            raise Exception("Redis connection fail")
