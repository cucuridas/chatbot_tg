from app.util.redis import RedisClient


CONN = RedisClient(1)
SERVICE_NAME = "WorkReport"


class WorkReport:
    async def service():
        pass

    async def returnMessage(value):
        return "</br> <h4> 업무보고용 파일을 첨부해주세요! 파일형식은 pptx만 가능하답니다"

    def checkValue(message):
        pass
