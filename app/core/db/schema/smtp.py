from pydantic import BaseModel


class ReqSmtpInfoSchema(BaseModel):
    send_mail: str
    send_password: str
    smtp_url: str
    smtp_port: int
    receive_mail: str


class ResSmtpInfoSchema(ReqSmtpInfoSchema):
    id: int

    class Config:
        orm_mode = True
