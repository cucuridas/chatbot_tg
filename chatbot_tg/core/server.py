from typing import Union
from fastapi import FastAPI
from api.v1 import message


def createApp() -> FastAPI:
    fastApiServer = FastAPI()
    fastApiServer.include_router(message.router)
    return fastApiServer


app: FastAPI = createApp()
