import sys
from app.util.controllRoominfo import ControllRoominfo

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.util.elasticsearch import Match, Document
from app.util.redis import RedisClient
from app.core.userinfo import User
from datetime import datetime
from app.util.parsing import ParsingData
import re

CONN = RedisClient(1)
SERVICE_NAME = "tgday"


class Tgday:
    async def service(message, roomId, conn=None):
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
            "</br> <h4> 정상적으로 등록되었습니다! 변경이 필요할 경우 'tgday'를 통해 다시 등록해주세요",
        )

    def checkValue(message):
        regex_value = re.compile(r"\d{4}\-\d{2}\-\d{2}")
        return bool(re.search(regex_value, message))

    async def getTgday(personId):
        return await Document().getDocument(personId, "tgday")

    async def returnMessage(value):
        return "</br> <h4> 날짜를 입력해주세요 [ex]2022-02-07\n "


class GetTgday:
    async def returnMessage(value):
        result_value = await GetTgday.getTgdayInfo(value["personId"])
        ControllRoominfo.deleteRoominfo(value["roomId"])
        if result_value != None:
            day_info = result_value["regist_date"]
            return f"</br> <h4>등록하신 TG day 날짜는 '{day_info}' 입니다<h4> "
        else:
            return f"</br> <h4> 등록하신 TG day가 존재하지 않아요! 'tgday' 서비스를 통해 등록해주세요!<h4>"

    async def getTgdayInfo(personId):
        value = await Document().getDocument(personId, SERVICE_NAME)
        if value == None:
            return None
        else:
            return ParsingData.parseDocument(value)

    async def getAllTgdayInfo():
        values = await Match().serarch("tgday")
        return_value = ""
        for value in values:
            return_value += f'이름: {value["name"]}  등록 날짜: {value["regist_date"]} \n'
        return return_value
