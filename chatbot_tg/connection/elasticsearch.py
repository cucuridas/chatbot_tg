from chatbot_tg.core.config import Settings
from chatbot_tg.abstract.connAbstract import Connect
from elasticsearch import Elasticsearch


class ElasticsearchConnection(Connect):
    """
    엘라스틱서치 connection을 만드는 클래스입니다
    """

    def getConenction(self):
        host = "http://{}:{}".format(Settings.ELASTCSEARCH_HOST, Settings.ELASTCSEARCH_PORT)
        self.conn = Elasticsearch(hosts=host, timeout=180)
        return self.conn

    def checkConnection(self):
        if self.conn.ping():
            return True
        else:
            raise Exception("Elasticsearch conenction faile")
