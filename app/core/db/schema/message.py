from pydantic import BaseModel


class ReqMessage(BaseModel):
    """
    fastapi의 Message API 호출시 사용하게되는 스키마 클래스 입니다
    """

    messageMarkdown: str


class ResSmtpInfoSchema(ReqMessage):
    """
    fastapi의 Message API 호출시 사용하게되는 스키마 클래스 입니다
    """

    class Config:
        orm_mode = True
