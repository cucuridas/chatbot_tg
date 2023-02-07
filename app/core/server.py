from typing import Union
from fastapi import FastAPI
from app.api.v1.message import router


def createApp() -> FastAPI:
    fastApiServer = FastAPI()
    fastApiServer.include_router(router)
    return fastApiServer


app: FastAPI = createApp()
