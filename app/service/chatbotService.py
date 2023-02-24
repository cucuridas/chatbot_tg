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


"""
chatbot을 통해 발생된 webhook을 처리하는 클래스입니다 서비스 클래스 앞에서 먼저 처리해야할 로직들을 처리합니다
ex) 서비스를 요청한 유저가 등록되어진 유저인가?, 진행중인 서비스에 알맞는 입력값이 전달되었는가?

"""

CONN = RedisClient(1)
SERVICE_VALUE = {
    None: None,
    "TGday": Tgday,
    "getTgday": GetTgday,
    "WorkReport": WorkReport,
}


class ChatbotService:
    async def checkService(message, conn=None):
        """
        webhook event를 통해 조회한 메세지 정보에서 유저가 원하는 서비스가 무엇인지 확인하여
        전달해주는 함수입니다 찾는 과정에서 user의 db 정보와 redis의 room 정보가 갱신됩니다

        Args:

            message (dict): webhook event를 data에 담긴 정보입니다
            conn (object, optional): 로직처리 후 chatbot을 통해 응답해주기위한 connection 객체입니다

        Returns:
            chatbot을 통해 메세지 전송
        """
        value = await Match().match(message["text"])
        if value is None:
            return conn.postMessage(
                message["roomId"], "</br> <h4>확인된 서비스가 없어요! 아직 제공중인 서비스가 아닌것 같네요~<h4>"
            )
        else:
            result = value["service"]
            redis_value = ControllRoominfo.addServiceRoominfo(message["roomId"], value)

            db = Session()
            user_info = db.query(Users).filter(Users.user_email == redis_value["personEmail"])
            user_info.update(
                {Users.user_room_info: message["roomId"], Users.user_id: message["personId"]}
            )

            ControllRoominfo.addServiceRoominfo(
                message["roomId"], {"user_name": user_info.first().user_name}
            )
            db.commit()

            redis_value.update({"roomId": message["roomId"]})
            return_service = await ChatbotService.returnMessage(SERVICE_VALUE[result], redis_value)

            return conn.postMessage(
                message["roomId"],
                f"요청하신 서비스가 '{result}' 인듯해요!\n 요청하신 서비스가 아니시라면 no[소문자]를 입력해주세요 \n {return_service}",
            )

    async def returnMessage(service, value):
        """

        Args:
            service (str): chatbot을 통해 요청한 서비스의 이름입니다
            value (object): 각 서비스에서 처리할 값이 담겨져 있습니다

        Returns:
            service.return : 각 서비스의 return 메세지가 str 형태로 전달됩니다
        """
        return await service.returnMessage(value)

    def checkRedisService(roomId):
        """
        roomId를 통해 해당 채팅방에서 요청한 서비스가 존재하는지 redis에서 조회합니다

        Args:
            roomId (str): chatbot을 통해 event가 발생한 roomId

        Returns:
            value["service"] : 서비스가 존재하면 서비스 이름을 str 타입으로 return
        """
        value = CONN.getContent(roomId)
        if value != None:
            if "service" in value:
                return value["service"]
        else:
            return None

    def replayService(roomId, conn):
        """chatbot을 통해 다른 서비스 요청이 왔을 시 처리하는 함수

        Args:
            roomId (str): webhook을 통해 evnet를 발생시킨 roomId
            conn (object): 응답을 해주기위한 connection 객체

        Returns:
            Success : str
        """
        conn.postMessage(roomId, "새로운 서비스를 입력해주세요~")
        ControllRoominfo.deleteRoominfo(roomId)
        return "Success"

    def checkValidation(servicename, message):
        """서비스에 적합한 파라미터가 전달되었는지를 확인하는 함수

        Args:
            servicename (str): chatbot을 통해 진행되고 있는 service 이름
            message (object): service를 통해 처리되어야하는 값

        Returns:
            bool
        """
        if servicename == None:
            return False
        else:
            return servicename.checkValue(message)

    def notCorrectValue(roomId, conn, service):
        """서비스에 맞지않는 값이 전달되었을 경우 Chatbot 사용자에게 메세지 전달

        Args:
            roomId (str): webhook을 통해 evnet를 발생시킨 roomId
            conn (object): 응답을 해주기위한 connection 객체
            service (str): chatbot을 통해 진행되고 있는 service 이름

        Returns:
           chatbot을 통해 메세지 전송
        """
        return conn.postMessage(
            roomId,
            f"'{service}'</br> <h4> 서비스에 맞지 않는 값이 입력되었거나 필요한 파일이 누락되었어요!\n 다시 입력해주세요~\n 원하시는 서비스가 아닐 경우 'no'를 입력해주세요 <h4>",
        )

    async def provideService(service, message, roomId, conn):
        """chatbot을 통해 요청되어진 서비스가 실제로 동작하는 비즈니스 로직

        Args:
            service (str): chatbot을 통해 진행되고 있는 service 이름
            message (object): service를 통해 처리되어야하는 값
            roomId (str): webhook을 통해 evnet를 발생시킨 roomId
            conn (object): 응답을 해주기위한 connection 객체

        Returns:
            success : str
        """
        await service.service(message, roomId, conn)
        ControllRoominfo.deleteRoominfo(roomId)
        return "Success"

    def checkUser(value, db: Session = Session()):
        """서비스를 요청한 user가 user 테이블에 등록되어진 user인지를 확인

        Args:
            value (dict): webhook event를 통해 전달되어진 event정보
            db (Session, optional): database 연결을 위한 session

        Returns:
            Bool
        """
        value = db.query(Users).filter(Users.user_email.like(value["personEmail"])).first()
        if value == None:
            return False
        else:
            return True

    def userFaliMessage(value, conn):
        """등록된 사용자가 아닐 경우 알림

        Args:
            value (dict): webhook event를 통해 전달되어진 event정보
            conn (object): 응답을 해주기위한 connection 객체

        """
        return conn.postMessage(
            value["roomId"],
            "</br> <h4> 등록되어진 사용자 정보가 아니예요 관리자에게 말씀하셔서 사용자 등록절차를 진행해주세요!",
        )
