from connection.elasticsearch import ElasticsearchConnection
from service.parsing import ParsingData


class ElasticClient:
    def __init__(self) -> None:
        self.conn = ElasticsearchConnection().getConenction()


class Match(ElasticClient):
    def __init__(self) -> None:
        super().__init__()

    async def match(self, inputText):
        query = {"match": {"service": inputText}}
        result = await self.conn.search(index="service_index", query=query)
        self.result = result["hits"]["hits"]
        return await self.checkResult()

    async def checkResult(self):
        if len(self.result) > 0:
            return ParsingData.parseElastic(self.result)
        else:
            return None
