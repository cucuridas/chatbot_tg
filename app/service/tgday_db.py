import re
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.core.db.base import Session
from app.service.controllRoominfo import ControllRoominfo
from app.service.redis import RedisClient
from app.core.db.models.tgday import Tgday as model_tg
from app.core.db.base import *
from datetime import date
from app.core.db.models.users import Users
from app.core.db.base import Session

CONN = RedisClient(1)
SERVICE_NAME = "tgday"


class Tgday:
    async def service(message, roomId, conn=None, db: Session = Session()):
        redis_value = CONN.getContent(roomId)
        year, month, day = message.split("-")
        value = db.query(Users).filter(Users.user_email.like("3310223@naver.com")).first()
        if value == None:
            return conn.postMessage(
                roomId,
                "</br> <h4> 등록되어진 사용자 정보가 아니예요 관리자에게 말씀하셔서 사용자 등록절차를 진행해주세요!",
            )
        data = {
            "user_name": value.user_name,
            "tgday_regist_day": date(year=int(year), month=int(month), day=int(day)),
            "user_id_webex": redis_value["personId"],
        }
        tgdayInfo = model_tg(**data)
        db.add(tgdayInfo)
        db.commit()
        return conn.postMessage(
            roomId,
            "</br> <h4> 정상적으로 등록되었습니다! 변경이 필요할 경우 'tgday'를 통해 다시 등록해주세요",
        )

    def checkValue(message):
        regex_value = re.compile(r"\d{4}\-\d{2}\-\d{2}")
        return bool(re.search(regex_value, message))

    async def returnMessage(value):
        return "</br> <h4> 날짜를 입력해주세요 [ex]2022-02-07\n "


class GetTgday:
    async def returnMessage(value, db: Session = Session()):
        ControllRoominfo.deleteRoominfo(value["roomId"])
        value = db.query(model_tg).filter(model_tg.user_id_webex == value["personId"]).first()
        if value != None:
            day_info = value.tgday_regist_day
            date_value = day_info.strftime("%y년 %m월 %d일")
            return f"</br> <h4>등록하신 TG day 날짜는 '{date_value}' 입니다<h4> "
        else:
            return f"</br> <h4> 등록하신 TG day가 존재하지 않아요! 'tgday' 서비스를 통해 등록해주세요!<h4>"
