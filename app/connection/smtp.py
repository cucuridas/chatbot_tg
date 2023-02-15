from email.message import EmailMessage
from email.mime.application import MIMEApplication
import os
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.db.models.smtp import SmtpInfoModel
from app.core.db.base import *
from app.service.tgday_db import MergeTgday
from datetime import datetime

smtp_info: SmtpInfoModel = Session().query(SmtpInfoModel).first()


class Smtp:
    def getConnection():
        smtp_hiworks = smtplib.SMTP(smtp_info.smtp_url, smtp_info.smtp_port)
        smtp_hiworks.ehlo()

        # 연결을 암호화
        smtp_hiworks.starttls()
        EMAIL_ADDR = smtp_info.send_mail
        EMAIL_PASSWORD = smtp_info.send_password

        # 2. SMTP 서버에 로그인
        smtp_hiworks.login(EMAIL_ADDR, EMAIL_PASSWORD)

        # 3. MIME 형태의 이메일 메세지 작성
        date = datetime.today().strftime("%m")
        message = MIMEMultipart()
        message["Subject"] = f"{date}월 tgday 종합본입니다 "
        message["From"] = EMAIL_ADDR  # 보내는 사람의 이메일 계정
        message["To"] = smtp_info.receive_mail
        content = f"""
안녕하십니까, 플랫폼 개발 3팀 최충은 프로입니다.
{date}월 플랫폼 개발3팀 tgday 종합본 입니다
감사합니다"""
        content_part = MIMEText(content, "plain")
        message.attach(content_part)

        MergeTgday.loadToCsv("플랫폼개발3팀")

        file_name = "플랫폼개발3팀_tgday.csv"
        with open(file_name, "rb") as excel_file:
            attachment = MIMEApplication(excel_file.read())
            # 첨부파일의 정보를 헤더로 추가
            attachment.add_header("Content-Disposition", "attachment", filename=file_name)
            message.attach(attachment)

        # 4. 서버로 메일 보내기
        smtp_hiworks.send_message(message)
        os.remove("플랫폼개발3팀_tgday.csv")
        # 5. 메일을 보내면 서버와의 연결 끊기
        smtp_hiworks.quit()
