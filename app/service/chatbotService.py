import sys
from app.core.db.base import Session

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.util.elasticsearch import Match, Document
from app.util.parsing import ParsingData
from app.util.redis import RedisClient
from app.service.tgdayDb import Tgday, GetTgday
from app.service.workReport import WorkReport
from app.core.db.models.users import Users
from app.core.db.base import *
from app.core.db.models.users import Users

# from app.service.tgday import Tgday, GetTgday
from app.util.controllRoominfo import ControllRoominfo

CONN = RedisClient(1)
SERVICE_VALUE = {
    None: None,
    "TGday": Tgday,
    "getTgday": GetTgday,
    "WorkReport": WorkReport,
}


class ChatbotService:
    async def checkService(roomId, message, conn=None):
        value = await Match().match(message)
        if value is None:
            return conn.postMessage(roomId, "</br> <h4>확인된 서비스가 없어요! 아직 제공중인 서비스가 아닌것 같네요~<h4>")
        else:
            result = value["service"]
            redis_value = ControllRoominfo.addServiceRoominfo(roomId, value)

            db = Session()
            user_info = db.query(Users).filter(Users.user_email == redis_value["personEmail"])
            user_info.update({"user_room_info": roomId})
            ControllRoominfo.addServiceRoominfo(roomId, {"user_name": user_info.first().user_name})
            db.commit()

            redis_value.update({"roomId": roomId})
            return_service = await ChatbotService.returnMessage(SERVICE_VALUE[result], redis_value)

            return conn.postMessage(
                roomId,
                f"요청하신 서비스가 '{result}' 인듯해요!\n 요청하신 서비스가 아니시라면 no[소문자]를 입력해주세요 \n {return_service}",
            )

    async def returnMessage(service, value):
        return await service.returnMessage(value)

    def checkRedisService(roomId):
        value = CONN.getContent(roomId)
        if value != None:
            if "service" in value:
                return value["service"]
        else:
            return None

    def replayService(roomId, conn):
        conn.postMessage(roomId, "새로운 서비스를 입력해주세요~")
        ControllRoominfo.deleteRoominfo(roomId)
        return "Success"

    def checkValidation(servicename, message):
        if servicename == None:
            return False
        else:
            return servicename.checkValue(message)

    def notCorrectValue(roomId, conn, service):
        return conn.postMessage(
            roomId,
            f"'{service}'</br> <h4> 서비스에 맞지 않는 값이 입력되었거나 필요한 파일이 누락되었어요!\n 다시 입력해주세요~\n 원하시는 서비스가 아닐 경우 'no'를 입력해주세요 <h4>",
        )

    async def provideService(service, message, roomId, conn):
        await service.service(message, roomId, conn)
        ControllRoominfo.deleteRoominfo(roomId)
        return "Success"

    def checkUser(value, db: Session = Session()):
        value = db.query(Users).filter(Users.user_email.like(value["personEmail"])).first()
        if value == None:
            return False
        else:
            return True

    def userFaliMessage(value, conn):
        return conn.postMessage(
            value["roomId"],
            "</br> <h4> 등록되어진 사용자 정보가 아니예요 관리자에게 말씀하셔서 사용자 등록절차를 진행해주세요!",
        )
