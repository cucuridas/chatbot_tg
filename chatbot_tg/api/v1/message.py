from fastapi import APIRouter, Request, Body, Depends, Path
import logging
from service.webex import Messages
from service.elasticsearch import Match

router: APIRouter = APIRouter()


@router.post("/", name="chatbot을 통해 전달 받는 message 처리")
async def result(request: Request):
    result = await request.json()
    messageObj = Messages()
    message = messageObj.getMessage(result["data"]["id"])
    messageObj.postMessage(message["roomId"], message["text"])
    print(message["text"])

    return logging.info("됨")
