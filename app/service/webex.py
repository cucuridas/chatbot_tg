from app.core.config import Settings
from app.service.redis import RedisClient
import requests, json
import logging


class WebexHook:
    """
    webe API connection을 만드는 클래스입니다
    """

    def __init__(self):
        self.url = "{}webhooks".format(Settings.WEBEX_API)
        self.header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + Settings.WEBEX_BOT_TOKEN,
        }

    def addHook(self):
        if self.checkHook():
            self.deleteHook()

        self.data = {
            "name": Settings.WEBHOOK_NAME,
            "targetUrl": Settings.WEBHOOK_URL,
            "resource": "messages",
            "event": "created",
        }

        response = requests.post(url=self.url, headers=self.header, data=json.dumps(self.data))
        response.raise_for_status()
        logging.info("Success,add webhook")

        RedisClient().setContent("hookinfo", json.loads(response.text))
        logging.info("Load data that response hookinofmation")
        return "Success"

    def deleteHook(self):
        url = "{}/{}".format(self.url, self.rd_value["id"])
        response = requests.delete(url=url, headers=self.header)
        return "Success"

    def checkHook(self):
        self.rd_value = RedisClient().getContent("hookinfo")
        if self.rd_value is None:
            return False
        else:
            return True


class Messages:
    """
    webex를 통한 event 발생 시 message 처리를 위한 클래스입니다
    """

    def __init__(self) -> None:
        self.url = "{}messages".format(Settings.WEBEX_API)
        self.header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + Settings.WEBEX_BOT_TOKEN,
        }

    def getMessage(self, dataId):
        url = "{}/{}".format(self.url, dataId)
        response = requests.get(url=url, headers=self.header)
        response.raise_for_status()

        return json.loads(response.text)

    def postMessage(self, roomId, value):
        data = {"roomId": roomId, "markdown": value}
        # header = self.header
        # header.setdefault("Accept", "application/json")
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.header)
        response.raise_for_status()
        return "Success"
