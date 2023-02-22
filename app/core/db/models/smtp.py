from sqlalchemy import Column, String, Date, Integer, BigInteger
from app.core.db.base import *


class SmtpInfoModel(Base):
    """
    smtpinfo table의 데이터를 불러와 사용하기위한 model 입니다
    """

    __tablename__ = "smtpinfo"
    id = Column(BigInteger, primary_key=True)
    send_mail = Column(String(200))
    send_password = Column(String(200))
    smtp_url = Column(String(200))
    smtp_port = Column(Integer())
    receive_mail = Column(String(200))
