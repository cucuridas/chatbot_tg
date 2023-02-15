from pydantic import BaseModel
from typing import Optional


class ReqTeamInfoSchema(BaseModel):
    team_name: str
    team_manager_email: str


class ResTeamInfoSchema(ReqTeamInfoSchema):
    team_id: int

    class Config:
        orm_mode = True
