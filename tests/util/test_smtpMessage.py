import os
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.service.tgday_db import MergeTgday
import datetime

from app.util.smtpMessage import SendMessage

# if __name__ == "__main__":
#     month = datetime.date.today().strftime("%m")
#     input_value = {
#         "title": "테스트 메일입니다",
#         "content": "테스트 메일입니다",
#         "csvFilePath": "./플랫폼개발3팀_tgday.csv",
#     }
#     MergeTgday.loadToCsv("플랫폼개발3팀")
#     SendMessage().writeEmail(**input_value)
#     os.remove("플랫폼개발3팀_tgday.csv")
