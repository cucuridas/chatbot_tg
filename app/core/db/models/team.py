from app.core.db.base import *
from sqlalchemy import BigInteger, Column, String, Date


class TeamModel(Base):
    __tablename__ = "team"

    team_id = Column(BigInteger, primary_key=True)
    team_name = Column(String(200), nullable=False, unique=True)
    team_manager_email = Column(String(200), nullable=True)
