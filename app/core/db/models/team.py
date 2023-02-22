from app.core.db.base import *
from sqlalchemy import BigInteger, Column, String, Date


class TeamModel(Base):
    """
    team table의 데이터를 불러와 사용하기위한 model 입니다
    """

    __tablename__ = "team"

    team_id = Column(BigInteger, primary_key=True)
    team_name = Column(String(200), nullable=False, unique=True)
    team_manager_email = Column(String(200), nullable=True)
