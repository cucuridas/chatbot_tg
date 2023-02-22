from pydantic import BaseModel
from typing import Optional
from datetime import date


class TgDay(BaseModel):
    """
    fastapi의 tgday API 호출시 사용하게되는 스키마 클래스 입니다
    """

    user_name: str
    tgday_regist_day: date
    user_id_webex: str
