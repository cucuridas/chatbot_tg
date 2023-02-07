import json
from app.service.elasticsearch import Match, Document
from app.service.parsing import ParsingData
from app.service.redis import RedisClient

CONN = RedisClient(1)


class ChatbotService:
    def checkService(roomId, value, conn=None):
        if value is None:
            return conn.postMessage(roomId, "확인된 서비스가 없어요! 아직 제공중인 서비스가 아닌것 같네요~")
        else:
            result = value["service"]
            return conn.postMessage(
                roomId,
                f"요청하신 서비스가 '{result}' 인듯해요!\n 맞으시면 날짜를 입력해주시고 [ex]2022-02-07\n 아니시라면 no[소문자]를 입력해주세요",
            )

    def checkRedisService(roomId):
        value = CONN.getContent(roomId)
        if value != None:
            if "service" in value:
                return value["service"]
        else:
            return None

    def replayService(roomId, conn):
        conn.postMessage(roomId, "새로운 서비스를 입력해주세요~")
