from rocketry import Grouper
from rocketry.conds import cron, after_success, daily, time_of_week, time_of_day, monthly
from app.connection.smtp import Smtp
from app.core.db.base import *
from app.core.db.models.users import Users
from app.util.webex import Messages

group: Grouper = Grouper()
messageObj = Messages()


@group.task(monthly.at("15th") & time_of_day.at("14:00"))
def send_mail():
    Smtp.getConnection()


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
