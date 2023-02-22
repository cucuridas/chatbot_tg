import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/home/cucuridas/chatbot")
from typing import Union
from fastapi import FastAPI
from app.api.v1.message import router
from app.api.v1.users import router as message_router
from app.api.v1.smtp import router as smtp_router
from app.api.v1.team import router as team_router
from app.api.v1.scheduler import router as scheduler_router
from app.util.webex import WebexHook


"""
fastapi 서버를 실행 시키는 파일입니다
"""


def createApp() -> FastAPI:
    WebexHook().addHook()
    fastApiServer = FastAPI()
    fastApiServer.include_router(router)
    fastApiServer.include_router(message_router)
    fastApiServer.include_router(smtp_router)
    fastApiServer.include_router(scheduler_router)
    fastApiServer.include_router(team_router)
    return fastApiServer


app: FastAPI = createApp()
