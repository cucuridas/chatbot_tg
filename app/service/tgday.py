import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.service.elasticsearch import Match, Document
from app.service.redis import RedisClient
from app.core.userinfo import User
from datetime import datetime
import re

CONN = RedisClient(1)
SERVICE_NAME = "tgday"


class Tgday:
    def serviceCheck(id):
        if id == "1":
            return "맞으시면 날짜를 입력해주시고 [ex]2022-02-07\n 아니시라면 no[소문자]를 입력해주세요"
        elif id == "2":
            return

    async def registTgDay(message, roomId, conn=None):
        redis_value = CONN.getContent(roomId)
        date = datetime.strptime(redis_value["created"], "%Y-%m-%dT%H:%M:%S.%fz")
        data = {
            "regist_time": date.strftime("%Y-%m-%dT%H:%M:%S"),
            "email": redis_value["personEmail"],
            "name": User.USER_INFO[redis_value["personEmail"]],
            "regist_date": message,
            "person_id": redis_value["personId"],
        }
        await Document().checkExistDoc("tgday", data)
        return conn.postMessage(
            roomId,
            "정상적으로 등록되었습니다! 변경이 필요할 경우 'tgday'를 통해 다시 등록해주세요",
        )

    def checkValue(message):
        regex_value = re.compile(r"\d{4}\-\d{2}\-\d{2}")
        return bool(re.search(regex_value, message))

    async def getTgday(personId):
        return await Document().getDocument(personId, "tgday")


class GetTgday:
    def getTgdayInfo(personId):
        value = Document().getDocument(SERVICE_NAME, personId)

        return value
