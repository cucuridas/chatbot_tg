from core.config import Settings
from service.redis import RedisClient
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
