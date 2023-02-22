import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from fastapi import APIRouter, Request, Body, Depends, Path
from app.core.config import Settings
import logging, json
from app.util.webex import Messages
from app.util.controllRoominfo import ControllRoominfo
from app.service.chatbotService import ChatbotService, SERVICE_VALUE
from app.core.db.schema.message import ReqMessage
from app.core.db.base import Session, get_db
from app.core.db.models.users import Users

router: APIRouter = APIRouter(tags=["Webex_Message"])
messageObj = Messages()


@router.post("/", name="chatbot을 통해 전달 받는 message 처리")
async def result(request: Request):
    result = await request.json()
    if result["data"]["personEmail"] != Settings.WEBEX_BOT_EMAIL:
        # 메세지 내용 파싱
        message = messageObj.getMessage(result["data"]["id"])
        # 필요 정보 변수에 저장
        room_info = ChatbotService.checkRedisService(result["data"]["roomId"])
        service = SERVICE_VALUE[room_info]
        # 해당 구문에서 캐시에 저장되어진 서비스 정보 유무와,서비스 별 입력 값  validation 필요
        if ChatbotService.checkValidation(service, message):
            await ChatbotService.provideService(service, message, message["roomId"], messageObj)
        else:
            if message["text"] == "no":
                ChatbotService.replayService(message["roomId"], messageObj)
            elif room_info != None:
                ChatbotService.notCorrectValue(message["roomId"], messageObj, "tgday")
            else:
                # room 정보 메모리에 저장
                ControllRoominfo.registRoominfo(result)
                if ChatbotService.checkUser(message):
                    await ChatbotService.checkService(
                        message["roomId"], message["text"], conn=messageObj
                    )
                else:
                    return ChatbotService.userFaliMessage(message, messageObj)
                # 결과 전송

    return logging.info("됨")


@router.post("/messagesend", name="message를 입력받아 chatbot을 통해 전달")
async def result(request: ReqMessage, db: Session = Depends(get_db)):
    results = db.query(Users.user_room_info).all()
    for result in results:
        if result.user_room_info == "" or result.user_room_info == None:
            continue
        else:
            messageObj.postMessage(
                result.user_room_info,
                request.messageMarkdown,
            )
    return "Success, Send Message : {}".format(request.messageMarkdown)
