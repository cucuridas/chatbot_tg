from app.core.db.schema.smtp import ReqSmtpInfoSchema, ResSmtpInfoSchema
from fastapi import APIRouter, Request, Body, Depends, Path
from typing import List
from app.util.smtp import smtpService
from app.core.db.base import *

router: APIRouter = APIRouter()


@router.post("/smtpregist", name="smtp 정보 변경", response_model=ReqSmtpInfoSchema)
async def updateSmtpInfo(req: ReqSmtpInfoSchema, db: Session = Depends(get_db)):
    return smtpService.updateSmtpInfo(req, db)


@router.get("/smtp", name="smtp 정보 조회", response_model=ResSmtpInfoSchema)
async def getSmtpInfo(db: Session = Depends(get_db)):
    return smtpService.getStmpInfo(db)
