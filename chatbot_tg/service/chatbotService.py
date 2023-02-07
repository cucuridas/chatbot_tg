from service.elasticsearch import Match
from service.parsing import ParsingData


class ChatbotService:
    async def checkService(roomId, value, conn=None):
        if value is None:
            return conn.messageObj.postMessage(roomId, "확인된 서비스가 없어요! 아직 제공중인 서비스가 아닌것 같네요")
        else:
            result = value["service"]
            return conn.messageObj.postMessage(
                roomId, f"요청하신 서비스가 {result}인듯해요 맞으면 'yes'[소문자]를 입력해주세요"
            )

    def checkServiceId():
        pass

    def registTgDay():
        pass

    def uploadBusinessReport():
        pass
