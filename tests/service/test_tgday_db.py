import sys
import asyncio


sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")


from app.service.tgday_db import Tgday, GetTgday, MergeTgday
import asyncio
from app.core.db.base import Session, Base


# MergeTgday.loadToCsv("플랫폼개발3팀")
# MergeTgday.test_load("플랫폼개발3팀")

# test_input = {
#     "message": "2022-02-24",
#     "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vM2Y3YTAxNjAtYTZjMi0xMWVkLThmNTMtNDVhNTg0YjU3NzQ5",
#     "conn": "sdsfds",
#     "db": Session(),
# }
# asyncio.run(Tgday.service(**test_input))

# GetTgday.loadToCsv()
