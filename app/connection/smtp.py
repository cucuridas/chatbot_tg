import os
import smtplib
from app.core.db.models.smtp import SmtpInfoModel
from app.core.db.base import *

from datetime import datetime

smtp_info: SmtpInfoModel = Session().query(SmtpInfoModel).first()


class SmtpConnetion:
    def __init__(self) -> None:
        self.smtp_hiworks = smtplib.SMTP(smtp_info.smtp_url, smtp_info.smtp_port)
        self.email_addr = smtp_info.send_mail
        self.email_password = smtp_info.send_password

    def getConnection(self):
        self.smtp_hiworks.ehlo()
        # 연결을 암호화
        self.smtp_hiworks.starttls()
        # 2. SMTP 서버에 로그인
        self.smtp_hiworks.login(self.email_addr, self.email_password)
