import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.core.config import Settings
from app.abstract.connAbstract import Connect
import redis


class RedisConnection(Connect):
    """
    레디스 connection을 만드는 클래스입니다
    """

    def getConenction(self, db=None):
        """
        .env 설정파일에 저장되어진 정보를 통해 redis와 연결하는 연결 객체를 생성합니다

        Args:
            db (int, optional): redis에서 접근할 db를 입력 받습니다

        Returns:
            self.conn: Redis
        """
        self.conn = redis.StrictRedis(
            host=Settings.REDIS_HOST, port=Settings.REDIS_PORT, db=db or 0
        )
        return self.conn

    def checkConnection(self):
        """
        생성되어진 redis 연결 객체를 통해 정상적으로 연결 되었는지를 확인하기 위한 함수입니다

        Returns:
            bool or Exception
        """
        if self.conn.ping():
            return True
        else:
            raise Exception("Redis connection fail")
