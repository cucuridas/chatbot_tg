class ParsingData:
    def prseWebhook(body):
        key = body["data"]["roomId"]
        value = body["data"]
        del value["roomId"]

        return key, value

    def parseElastic(hits):
        return hits[0]["_source"]
