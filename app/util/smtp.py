from app.connection.smtp import Smtp
from app.core.db.base import *
from app.core.db.schema.smtp import ReqSmtpInfoSchema
from app.core.db.models.smtp import SmtpInfoModel


class smtpService:
    def updateSmtpInfo(req: ReqSmtpInfoSchema, db: Session = Session()):
        db.query(SmtpInfoModel).filter(SmtpInfoModel.id == 1).update(req.dict())
        db.commit()

        return req.dict()

    def getStmpInfo(db: Session):
        return db.query(SmtpInfoModel).first()
