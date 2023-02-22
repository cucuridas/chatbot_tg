from pydantic import BaseModel


class ReqSmtpInfoSchema(BaseModel):
    """
    fastapi의 smtp API 호출시 사용하게되는 스키마 클래스 입니다
    """

    send_mail: str
    send_password: str
    smtp_url: str
    smtp_port: int
    receive_mail: str


class ResSmtpInfoSchema(ReqSmtpInfoSchema):
    """
    fastapi의 smtp API 호출시 사용하게되는 스키마 클래스 입니다
    """

    id: int

    class Config:
        orm_mode = True
