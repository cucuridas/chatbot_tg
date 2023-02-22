import datetime
import os
from rocketry import Grouper
from rocketry.conds import cron, after_success, daily, time_of_week, time_of_day, monthly
from app.core.db.base import *
from app.core.db.models.users import Users
from app.util.webex import Messages
from app.service.workReport import MergeWorkReport
from app.service.tgdayDb import SendMergedTgday


group: Grouper = Grouper()
messageObj = Messages()


@group.task(monthly.at("3rd") & time_of_day.at("14:00"))
def send_mail():
    SendMergedTgday.sendMail("플랫폼개발3팀")


@group.task(daily & (time_of_week.at("Fri") & time_of_day.at("09:40")))
def sendWorkReportMail():
    MergeWorkReport.makeMergePPTX()
    MergeWorkReport.sendMail("플랫폼개발3팀")


@group.task(daily & (time_of_week.at("Fri") & time_of_day.at("09:00")))
def sendWorkReport(db=Session()):
    results = db.query(Users.user_room_info).all()
    for result in results:
        if result.user_room_info == "" or result.user_room_info == None:
            continue
        else:
            messageObj.postMessage(
                result.user_room_info,
                "</br> <h4> 주간 업무보고서 종합하는 날이에요, '업무 보고'를 입력해서 저에게 파일을 전달해주세요! \n 종합은 9시 40분에 마갑되어 자동적으로 발송됩니다!",
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
