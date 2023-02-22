import os
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.core.config import Settings, WorkReportSettings
from app.util.redis import RedisClient
from app.util.createDate import CreateDatetime
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

    def downloadFile(self, fileUrl):
        """
        https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL0NPTlRFTlQvMTkwZmU2NDAtYWU4MS0xMWVkLWJjMzItMmRmYTZmYTU4NTNiLzA
        """

        # webex cloud에서 파일 정보 바이너리 형태로 받아오기
        response = requests.get(url=fileUrl, headers=self.header)
        response.raise_for_status()

        return response.content

    # 주간에 다른날짜로 들어왔을시 처리할 로직이 필요
    def saveFiletoPptx(content, userName):
        # 날짜 정보 수집
        today = CreateDatetime.today()
        weekTody = CreateDatetime.todayToWeek(today["year"], today["month"], today["day"])
        fileName = "{}/{}주차/{}_{}_{}주차_{}.pptx".format(
            WorkReportSettings.WORK_REPORT_SAVE_POINT,
            weekTody,
            today["year"],
            today["month"],
            weekTody,
            userName,
        )
        # 서버 workReport 디렉토리에 저장
        Messages.checkDirectory(weekTody)
        # os.mkfifo(fileName)
        with open(fileName, "wb") as f:
            f.write(content)

        return "Success"

    def checkDirectory(weekTody, dirPath: str = WorkReportSettings.WORK_REPORT_SAVE_POINT):
        Messages.checkRootDirectory()
        pathValue = f"{dirPath}/{weekTody}주차"
        if os.path.exists(pathValue):
            return True
        else:
            os.mkdir(pathValue)

    def checkRootDirectory(dirPath: str = WorkReportSettings.WORK_REPORT_SAVE_POINT):
        if os.path.exists(dirPath):
            return True
        else:
            return os.mkdir(dirPath)
