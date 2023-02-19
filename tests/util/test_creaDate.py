import os
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")

from app.util.createDate import CreateDatetime

value = CreateDatetime.today()
CreateDatetime.todayToWeek(value["year"], 3, 16)
