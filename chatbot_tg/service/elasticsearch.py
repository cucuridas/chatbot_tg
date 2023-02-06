from connection.elasticsearch import ElasticsearchConnection


class ElasticClient:
    def __init__(self) -> None:
        self.conn = ElasticsearchConnection().getConenction()


class Match(ElasticClient):
    def __init__(self) -> None:
        super().__init__()

    def match(self, inputText):
        query = {"match": {"service": inputText}}
        self.result = self.conn.search(index="service_index", query=query)

    def checkResult(self):
        if len(self.result["hits"]["hits"]) > 0:
            return True
        else:
            return False
