from sqlalchemy import Column, String, Date, Integer, BigInteger
from app.core.db.base import *


class SmtpInfoModel(Base):
    __tablename__ = "smtpinfo"
    id = Column(BigInteger, primary_key=True)
    send_mail = Column(String(200))
    send_password = Column(String(200))
    smtp_url = Column(String(200))
    smtp_port = Column(Integer())
    receive_mail = Column(String(200))
