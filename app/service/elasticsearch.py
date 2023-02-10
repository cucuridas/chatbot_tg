import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.connection.elasticsearch import ElasticsearchConnection
from app.service.parsing import ParsingData


class ElasticClient:
    def __init__(self) -> None:
        self.conn = ElasticsearchConnection().getConenction()


class Match(ElasticClient):
    def __init__(self) -> None:
        super().__init__()

    async def match(
        self,
        inputText,
        index="service_index",
    ):
        query = {"match": {"service": inputText}}
        result = await self.conn.search(index=index, query=query)
        self.result = result["hits"]["hits"]
        return await self.checkResult()

    async def serarch(self, index):
        result = await self.conn.search(index=index)
        self.result = result["hits"]["hits"]
        return await self.checkResult()

    async def checkResult(self):
        if len(self.result) == 1:
            return ParsingData.parseElastic(self.result)
        elif len(self.result) > 1:
            return ParsingData.parseElasticIter(self.result)
        else:
            return None


class Document(ElasticClient):
    def __init__(self) -> None:
        super().__init__()

    async def getDocument(self, id, index):
        if await self.conn.exists(index=index, id=id):
            return None
        else:
            return await self.conn.get(index=index, id=id)

    async def putDocument(self, index, data):
        if await self.conn.indices.exists(index=index):
            await self.conn.index(index=index, body=data, id=data["person_id"])
        else:
            await self.conn.indices.create(index=index)
            await self.conn.index(index=index, body=data, id=data["person_id"])

    async def updateDocument(self, index, data):
        update_data = {"doc": data}
        return await self.conn.update(index=index, id=data["person_id"], body=update_data)

    async def checkExistDoc(
        self,
        serviceName,
        data,
    ):
        if await self.conn.exists(index=serviceName, id=data["person_id"]):
            return await self.updateDocument(serviceName, data)
        else:
            return await self.putDocument(serviceName, data)
