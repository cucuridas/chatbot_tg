from pydantic import BaseModel
from typing import Optional


class ReqTeamInfoSchema(BaseModel):
    """
    fastapi의 team API 호출시 사용하게되는 스키마 클래스 입니다
    """

    team_name: str
    team_manager_email: str


class ResTeamInfoSchema(ReqTeamInfoSchema):
    """
    fastapi의 team API 호출시 사용하게되는 스키마 클래스 입니다
    """

    team_id: int

    class Config:
        orm_mode = True
