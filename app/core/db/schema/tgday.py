from pydantic import BaseModel
from typing import Optional
from datetime import date


class TgDay(BaseModel):
    user_name: str
    tgday_regist_day: date
    user_id_webex: str
