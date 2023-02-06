from fastapi import APIRouter, Request, Body, Depends, Path
import logging

router: APIRouter = APIRouter()


@router.post("/", name="chatbot을 통해 전달 받는 message 처리")
async def result(request: Request):
    print(await request.json())
    return logging.info("됨")
