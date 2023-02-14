from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    # id: int
    user_name: str
    user_email: str
    user_id_webex: Optional[str] = None
    user_team: str


class ResponseUsers(UserBase):
    id: int

    class Config:
        orm_mode = True
