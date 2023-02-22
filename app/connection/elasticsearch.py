import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.core.config import Settings
from app.abstract.connAbstract import Connect
from elasticsearch import AsyncElasticsearch


class ElasticsearchConnection(Connect):
    """
    엘라스틱서치 connection을 만드는 클래스입니다
    """

    def getConenction(self):
        """
        .env에 저장되어진 elasticsearch 연결을 위한 정보들을 활용하여 elasticsearch connetion을 비동기 처리 객체 형태로 전달받아 return합니다

        Returns:
            self.conn : AsyncElasticsearch(host=host)
        """
        host = "http://{}:{}".format(Settings.ELASTCSEARCH_HOST, Settings.ELASTCSEARCH_PORT)
        self.conn = AsyncElasticsearch(hosts=host, timeout=180)
        return self.conn

    def checkConnection(self):
        """
        'getConnetcion' 함수를 호출한 뒤 elasticsearch와 정상적으로 연결이 되었는지를 확인하기위한 함수입니다

        Returns:
            bool or Exception
        """
        if self.conn.ping():
            return True
        else:
            raise Exception("Elasticsearch conenction faile")
