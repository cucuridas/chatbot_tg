import uuid
from sqlalchemy import Column, String
from app.core.db.base import *


class Users(Base):
    __tablename__ = "users"

    id = Column(String(120), primary_key=True, default=str(uuid.uuid4()))
    user_name = Column(String(80), nullable=False)
    user_email = Column(String(300), nullable=False)
    user_id_webex = Column(String(1000))
    user_team = Column(String(20), nullable=False)
