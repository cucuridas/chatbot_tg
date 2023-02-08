import json
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.service.elasticsearch import Match, Document
from app.service.parsing import ParsingData
from app.service.redis import RedisClient
from app.service.tgday import Tgday, GetTgday


CONN = RedisClient(1)


class ChatbotService:
    service_value = {"tgday": Tgday, "gettgday": GetTgday}

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

    def checkValidation(servicename, message):
        return servicename.checkValue(message)

    def notCorrectValue(roomId, conn, service):
        return conn.postMessage(
            roomId,
            f"'{service}' 서비스에 맞지 않는 값이 입력되었어요!\n 다시 입력해주세요~\n 원하시는 서비스가 아닐 경우 'no'를 입력해주세요 ",
        )
