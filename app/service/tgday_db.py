import datetime
import os
import re
import sys
import csv

from sqlalchemy import and_

from app.util.smtpMessage import SendMessage

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.core.db.base import Session
from app.util.controllRoominfo import ControllRoominfo
from app.util.redis import RedisClient
from app.core.db.base import *
from datetime import date
from app.core.db.models.users import Users
from app.core.db.models.tgday import Tgday as model_tg
from app.core.db.models.team import TeamModel
from app.core.db.base import Session


CONN = RedisClient(1)
SERVICE_NAME = "tgday"


class Tgday:
    async def service(message, roomId, conn, db: Session = Session()):
        redis_value = CONN.getContent(roomId)
        year, month, day = message.split("-")
        registDate = date(year=int(year), month=int(month), day=int(day))
        webexId = redis_value["personId"]

        value = db.query(Users).filter(Users.user_email.like(redis_value["personEmail"])).first()

        if Tgday.checkTgday(db, value.user_name):
            Tgday.updateTgday(value.user_name, registDate, conn, roomId, db)
        else:
            Tgday.registTgday(value.user_name, registDate, webexId, conn, roomId, db)

    def checkTgday(db, userName):
        if db.query(model_tg).filter(model_tg.user_name == userName).first() != None:
            return True
        else:
            return False

    def registTgday(userName, registDate, webexId, conn, roomId, db):
        data = {
            "user_name": userName,
            "tgday_regist_day": registDate,
            "user_id_webex": webexId,
        }
        tgdayInfo = model_tg(**data)
        db.add(tgdayInfo)
        db.commit()
        return conn.postMessage(
            roomId,
            "</br> <h4> 정상적으로 등록되었습니다! 변경이 필요할 경우 'tgday'를 통해 다시 등록해주세요",
        )

    def updateTgday(userName, registDate, conn, roomId, db):
        db.query(model_tg).filter(model_tg.user_name == userName).update(
            {model_tg.tgday_regist_day: registDate}
        )
        db.commit()
        return conn.postMessage(
            roomId,
            "</br> <h4> 정상적으로 변경되었습니다! 변경이 필요할 경우 'tgday'를 통해 다시 등록해주세요",
        )

    def checkValue(message):
        regex_value = re.compile(r"\d{4}\-\d{2}\-\d{2}")
        return bool(re.search(regex_value, message))

    async def returnMessage(value):
        return "</br> <h4> 날짜를 입력해주세요 [ex]2022-02-07\n "


class GetTgday:
    async def returnMessage(value, db: Session = Session()):
        ControllRoominfo.deleteRoominfo(value["roomId"])
        value = db.query(model_tg).filter(model_tg.user_id_webex == value["personId"]).first()
        if value != None:
            day_info = value.tgday_regist_day
            date_value = day_info.strftime("%y년 %m월 %d일")
            return f"</br> <h4>등록하신 TG day 날짜는 '{date_value}' 입니다<h4> "
        else:
            return f"</br> <h4> 등록하신 TG day가 존재하지 않아요! 'tgday' 서비스를 통해 등록해주세요!<h4>"


class MergeTgday:
    def loadToCsv(team_name):
        outfile = open(f"./{team_name}_tgday.csv", "w", encoding="utf-8-sig")
        outcsv = csv.writer(outfile)
        outcsv.writerow(["이름", "팀명", "날짜"])

        records = MergeTgday.getTgdayfilterTeam(team_name)
        for record in records:
            outcsv.writerow(list(record))

        outfile.close()

    def getTgdayfilterTeam(team_name, db: Session = Session()):
        values = (
            db.query(Users.user_name, Users.user_team, model_tg.tgday_regist_day)
            .filter(and_(team_name == Users.user_team, Users.user_name == model_tg.user_name))
            .all()
        )
        return values


class SendMergedTgday:
    def sendMail(teamName):
        month = datetime.date.today().strftime("%m")
        input_value = {
            "title": f"{month}월 tgday 종합입니다",
            "content": f"""
                        안녕하십니까, {teamName} 담당자입니다.
                        {month}월 {teamName} tgday 종합본 입니다
                        감사합니다""",
            "csvFilePath": f"./{teamName}_tgday.csv",
        }
        MergeTgday.loadToCsv(teamName)
        SendMessage().writeEmail(**input_value)
        os.remove(f"{teamName}_tgday.csv")
