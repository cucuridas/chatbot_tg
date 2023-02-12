import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from typing import Union
from fastapi import FastAPI
from app.api.v1.message import router
from app.api.v1.users.users import router as message_router
from app.service.webex import WebexHook


def createApp() -> FastAPI:
    WebexHook().addHook()
    fastApiServer = FastAPI()
    fastApiServer.include_router(router)
    fastApiServer.include_router(message_router)
    return fastApiServer


app: FastAPI = createApp()
