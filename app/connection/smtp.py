import os
import smtplib
from app.core.db.models.smtp import SmtpInfoModel
from app.core.db.base import *

from datetime import datetime

smtp_info: SmtpInfoModel = Session().query(SmtpInfoModel).first()


class SmtpConnetion:
    """
    메일 전송을 위한 smtp 정보를 받아와 smtp 연결 객체를 만드는 클래스입니다
    """

    def __init__(self) -> None:
        """
        Args :
            smtp_hiworks:  smtp 서버의 정보를 받아옵니다

            email_addr: 보낼때 사용하게될 이메일 정보를 받아옵니다

            email_password: 보낼때 사용하게될 비밀번호 정보를 받아옵니다
        """
        self.smtp_hiworks = smtplib.SMTP(smtp_info.smtp_url, smtp_info.smtp_port)
        self.email_addr = smtp_info.send_mail
        self.email_password = smtp_info.send_password

    def getConnection(self):
        """
        SmtpConnection 객체를 생성한 뒤 객체의 속성 값을 통해 smtp 서버와 연결하는 함수입니다
        """
        self.smtp_hiworks.ehlo()
        # 연결을 암호화
        self.smtp_hiworks.starttls()
        # 2. SMTP 서버에 로그인
        self.smtp_hiworks.login(self.email_addr, self.email_password)
