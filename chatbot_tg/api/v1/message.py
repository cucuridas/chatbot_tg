from fastapi import APIRouter, Request, Body, Depends, Path
from core.config import Settings
import logging, json
from service.webex import Messages
from service.controllRoominfo import ControllRoominfo
from service.elasticsearch import Match
from service.chatbotService import ChatbotService

router: APIRouter = APIRouter()
messageObj = Messages()


@router.post("/", name="chatbot을 통해 전달 받는 message 처리")
async def result(request: Request):
    result = await request.json()
    if result["data"]["personEmail"] != Settings.WEBEX_BOT_EMAIL:
        # room 정보 메모리에 저장
        ControllRoominfo.registRoominfo(result)
        # 메세지 내용 파싱
        message = messageObj.getMessage(result["data"]["id"])
        # 서비스 정보 업데이트
        value = await Match().match(message["text"])
        ControllRoominfo.updateRomminfo(message["roomId"], value)
        # 결과 전송
        ChatbotService.checkService(message["roomId"], value, conn=messageObj)

    return logging.info("됨")
