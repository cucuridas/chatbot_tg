from email.message import EmailMessage
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Smtp:
    def getConnection():
        smtp_hiworks = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_hiworks.ehlo()

        # 연결을 암호화
        smtp_hiworks.starttls()
        EMAIL_ADDR = "cucuridas@gmail.com"
        EMAIL_PASSWORD = "fxqifswyhscvszrp"

        # 2. SMTP 서버에 로그인
        smtp_hiworks.login(EMAIL_ADDR, EMAIL_PASSWORD)

        # 3. MIME 형태의 이메일 메세지 작성
        message = EmailMessage()
        message.set_content(
            """
안녕하십니까, 플랫폼 개발 3팀 최충은 프로입니다.
플랫폼 개발3팀 tgday 종합본 입니다
감사합니다"""
        )
        message["Subject"] = "test 메일"
        message["From"] = EMAIL_ADDR  # 보내는 사람의 이메일 계정
        message["To"] = "ce.choi@time-gate.com"

        # 4. 서버로 메일 보내기
        smtp_hiworks.send_message(message)

        # 5. 메일을 보내면 서버와의 연결 끊기
        smtp_hiworks.quit()
