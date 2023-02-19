from app.core.db.base import Session
from app.util.redis import RedisClient
from app.util.webex import Messages
from app.core.db.models.users import Users

CONN = RedisClient(1)
SERVICE_NAME = "WorkReport"


class WorkReport:
    async def service(message, roomId, conn):
        redis_value = CONN.getContent(roomId)

        content = Messages().downloadFile(message["files"][0])
        Messages.saveFiletoPptx(content, redis_value["user_name"])
        value = Session
        return conn.postMessage(
            roomId,
            "</br> <h4> 업무보고 파일을 정상적으로 서버에 저장하였어요! \n 수정하시고 싶으시다면 '업무보고 파일 변경' 서비스를 통해 다시 파일을 전송해주세요! \n 종합 마감은 금요일 10시입니다!",
        )

    async def returnMessage(value):
        return "</br> <h4> 업무보고용 파일을 첨부해주세요! 파일형식은 pptx만 가능하답니다"

    def checkValue(message):
        if "files" not in message:
            return False
        else:
            return True
