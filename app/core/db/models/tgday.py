import uuid
from sqlalchemy import Column, String, Date
from app.core.db.base import *


class Tgday(Base):
    """
    tgday table의 데이터를 불러와 사용하기위한 model 입니다
    """

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    __tablename__ = "tgday"

    user_name = Column(String(80), primary_key=True, nullable=False)
    tgday_regist_day = Column(Date())
    # user_id_webex = Column(String(1000))
