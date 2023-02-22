from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """
    fastapi의 user API 호출시 사용하게되는 스키마 클래스 입니다
    """

    # id: int
    user_name: str
    user_email: str
    user_room_info: Optional[str] = None
    user_team: str


class ResponseUsers(UserBase):
    """
    fastapi의 user API 호출시 사용하게되는 스키마 클래스 입니다
    """

    id: int

    class Config:
        orm_mode = True
