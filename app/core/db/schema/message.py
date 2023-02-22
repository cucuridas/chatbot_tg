from pydantic import BaseModel


class ReqMessage(BaseModel):
    messageMarkdown: str


class ResSmtpInfoSchema(ReqMessage):
    class Config:
        orm_mode = True
