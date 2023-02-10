import sys
import asyncio

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")


from app.service.tgday import Tgday, GetTgday


asyncio.run(GetTgday.getAllTgdayInfo())
