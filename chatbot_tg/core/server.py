from typing import Union
from fastapi import FastAPI


def createApp() -> FastAPI:
    fastApiServer = FastAPI()
    return fastApiServer


app: FastAPI = createApp()
