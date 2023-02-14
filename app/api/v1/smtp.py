from app.core.db.schema.smtp import ReqSmtpInfoSchema
from fastapi import APIRouter, Request, Body, Depends, Path
from typing import List
from app.service.smtp import smtpService
from app.core.db.base import *

router: APIRouter = APIRouter()


@router.post("/smtp", name="smtp 정보 변경", response_model=ReqSmtpInfoSchema)
async def register_users(req: ReqSmtpInfoSchema, db: Session = Depends(get_db)):
    return smtpService.updateSmtpInfo(req, db)
