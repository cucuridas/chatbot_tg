import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")


class ParsingData:
    def prseWebhook(body):
        key = body["data"]["roomId"]
        value = body["data"]
        del value["roomId"]

        return key, value

    def parseElastic(hits):
        return hits[0]["_source"]

    def parseElasticIter(hits):
        return [hit["_source"] for hit in hits]

    def parseDocument(value):
        return value["_source"]
