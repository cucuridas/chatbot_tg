import re
import sys
from app.service.controllRoominfo import ControllRoominfo
from app.service.redis import RedisClient
from app.core.db.models.tgday import Tgday


sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")

CONN = RedisClient(1)
SERVICE_NAME = "tgday"


class Tgday:
    async def service(message, roomId, conn=None):
        redis_value = CONN.getContent(roomId)
        pass

    def checkValue(message):
        regex_value = re.compile(r"\d{4}\-\d{2}\-\d{2}")
        return bool(re.search(regex_value, message))

    async def getTgday(personId):
        pass

    async def returnMessage(value):
        return "</br> <h4> 날짜를 입력해주세요 [ex]2022-02-07\n "


class GetTgday:
    async def returnMessage(value):
        pass
