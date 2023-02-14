import uuid
from sqlalchemy import Column, String, BigInteger
from app.core.db.base import *


class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    user_name = Column(String(80), nullable=False)
    user_email = Column(String(300), nullable=False)
    user_room_info = Column(String(1000))
    user_team = Column(String(20), nullable=False)
