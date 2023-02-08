import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")


from app.service.tgday import Tgday


print(Tgday.checkValue("2022-03-03"))
