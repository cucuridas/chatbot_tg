import datetime
import os
from rocketry import Grouper
from rocketry.conds import cron, after_success, daily, time_of_week, time_of_day, monthly
from app.core.db.base import *
from app.core.db.models.users import Users
from app.util.webex import Messages
from app.service.tgday_db import MergeTgday
from app.util.smtpMessage import SendMessage

group: Grouper = Grouper()
messageObj = Messages()


@group.task(monthly.at("3rd") & time_of_day.at("14:00"))
def send_mail():
    month = datetime.date.today().strftime("%m")
    input_value = {
        "title": f"{month}월 tgday 종합입니다",
        "content": f"""
                    안녕하십니까, 플랫폼 개발 3팀 최충은 프로입니다.
                    {month}월 플랫폼 개발3팀 tgday 종합본 입니다
                    감사합니다""",
        "csvFilePath": "./플랫폼개발3팀_tgday.csv",
    }
    MergeTgday.loadToCsv("플랫폼개발3팀")
    SendMessage().writeEmail(**input_value)
    os.remove("플랫폼개발3팀_tgday.csv")


@group.task(daily & (time_of_week.at("Fri") & time_of_day.at("09:00")))
def sendWorkReport(db=Session()):
    results = db.query(Users.user_room_info).all()
    for result in results:
        if result.user_room_info == "" or result.user_room_info == None:
            continue
        else:
            messageObj.postMessage(
                result.user_room_info,
                "</br> <h4> 주간 업무보고서 종합하는 날입니다!, 최충은프로에게 전달해주세요",
            )


@group.task(monthly.at("1st") & time_of_day.at("09:00"))
def sendTgday(db=Session()):
    results = db.query(Users.user_room_info).all()
    for result in results:
        if result.user_room_info == "" or result.user_room_info == None:
            continue
        else:
            messageObj.postMessage(
                result.user_room_info,
                "</br> <h4> tgday 종합하는 날입니다!, 저에게 'tgday'를 입력해서 원하는 날짜를 등록해주세요!\n 수정은 월 3일까지입니다!",
            )
