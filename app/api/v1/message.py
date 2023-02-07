from fastapi import APIRouter, Request, Body, Depends, Path
from app.service.tgday import Tgday
from app.core.config import Settings
import logging, json
from app.service.webex import Messages
from app.service.controllRoominfo import ControllRoominfo
from app.service.elasticsearch import Match
from app.service.chatbotService import ChatbotService

router: APIRouter = APIRouter()
messageObj = Messages()


@router.post("/", name="chatbot을 통해 전달 받는 message 처리")
async def result(request: Request):
    result = await request.json()
    if result["data"]["personEmail"] != Settings.WEBEX_BOT_EMAIL:
        # 메세지 내용 파싱
        message = messageObj.getMessage(result["data"]["id"])
        if (
            ChatbotService.checkRedisService(result["data"]["roomId"]) != None
            and message["text"] != "no"
        ):
            await Tgday.registTgDay(message["text"], message["roomId"], messageObj)
            ControllRoominfo.deleteRoominfo(message["roomId"])
        else:
            if message["text"] == "no":
                ChatbotService.replayService(message["roomId"], messageObj, messageObj)
                ControllRoominfo.deleteRoominfo(message["roomId"])
            else:
                # room 정보 메모리에 저장
                ControllRoominfo.registRoominfo(result)
                # 서비스 정보 업데이트
                value = await Match().match(message["text"])
                ControllRoominfo.updateRoominfo(message["roomId"], value)
                # 결과 전송
                ChatbotService.checkService(message["roomId"], value, conn=messageObj)

    return logging.info("됨")
