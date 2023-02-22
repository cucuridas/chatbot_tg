from email.mime.application import MIMEApplication
from app.connection.smtp import SmtpConnetion, smtp_info
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Optional


class SendMessage(SmtpConnetion):
    def __init__(self) -> None:
        super().__init__()
        self.getConnection()

    def writeEmail(self, title, content, filePath: Optional[str] = None):
        message = MIMEMultipart()
        message["Subject"] = title
        message["From"] = self.email_addr  # 보내는 사람의 이메일 계정
        message["To"] = smtp_info.receive_mail
        content = content
        content_part = MIMEText(content, "plain")
        message.attach(content_part)

        if filePath != None:
            with open(filePath, "rb") as csv_file:
                attachment = MIMEApplication(csv_file.read())
                # 첨부파일의 정보를 헤더로 추가
                filename = filePath.split("/")[-1]
                attachment.add_header("Content-Disposition", "attachment", filename=filename)
                message.attach(attachment)

        # 4. 서버로 메일 보내기
        self.smtp_hiworks.send_message(message)
        # 5. 메일을 보내면 서버와의 연결 끊기
        self.smtp_hiworks.quit()
