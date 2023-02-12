import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from fastapi import APIRouter, Request, Body, Depends, Path
from app.service.tgday import Tgday, GetTgday
from app.core.config import Settings
import logging, json
from app.service.webex import Messages
from app.service.controllRoominfo import ControllRoominfo
from app.service.elasticsearch import Match
from app.service.chatbotService import ChatbotService, SERVICE_VALUE


router: APIRouter = APIRouter()
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
        if ChatbotService.checkValidation(service, message["text"]):
            await ChatbotService.provideService(
                service, message["text"], message["roomId"], messageObj
            )
        else:
            if message["text"] == "no":
                ChatbotService.replayService(message["roomId"], messageObj)
            elif room_info != None:
                ChatbotService.notCorrectValue(message["roomId"], messageObj, "tgday")
            else:
                # room 정보 메모리에 저장
                ControllRoominfo.registRoominfo(result)
                # 결과 전송
                await ChatbotService.checkService(
                    message["roomId"], message["text"], conn=messageObj
                )

    return logging.info("됨")
