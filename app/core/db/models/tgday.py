import uuid
from sqlalchemy import Column, String, Date
from app.core.db.base import *


class Tgday(Base):
    __tablename__ = "tgday"

    user_name = Column(String(80), primary_key=True, nullable=False)
    tgday_regist_day = Column(Date())
    user_id_webex = Column(String(1000))
