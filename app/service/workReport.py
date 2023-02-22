import copy
import os
from app.core.db.base import Session
from app.util.redis import RedisClient
from app.util.webex import Messages
from app.core.db.models.users import Users
from pptx import Presentation
from pptx.shapes.graphfrm import GraphicFrame
from pptx.shapes.autoshape import Shape

CONN = RedisClient(1)
SERVICE_NAME = "WorkReport"
DEFALUT_FROM = "./form.pptx"


class WorkReport:
    async def service(message, roomId, conn):
        redis_value = CONN.getContent(roomId)

        content = Messages().downloadFile(message["files"][0])
        Messages.saveFiletoPptx(content, redis_value["user_name"])
        value = Session
        return conn.postMessage(
            roomId,
            "</br> <h4> 업무보고 파일을 정상적으로 서버에 저장하였어요! \n 수정하시고 싶으시다면 '업무보고' 서비스를 통해 다시 파일을 전송해주세요! \n 종합 마감은 금요일 10시입니다!",
        )

    async def returnMessage(value):
        return "</br> <h4> 업무보고용 파일을 첨부해주세요! 파일형식은 pptx만 가능하답니다"

    def checkValue(message):
        if "files" not in message:
            return False
        else:
            return True


class MergeWorkReport:
    def makeMergePPTX():
        main_pptObj = Presentation(DEFALUT_FROM)
        fileList = os.listdir("./workReport")

        for fileName in fileList:
            slide = MergeWorkReport.copySlide(f"./workReport/{fileName}")
            # copy_slide = main_pptObj.slides.add_slide(main_pptObj.slide_layouts[6])
            copy_slide = main_pptObj.slides[2]
            # copy_slide = main_pptObj.slides.add_slide(slide)
            for element in slide:
                copy_slide.shapes._spTree.insert_element_before(element, "p:extLst")
            main_pptObj.slides.add_slide(copy_slide)
            main_pptObj.save(DEFALUT_FROM)

    def copySlide(path):
        pptObj = Presentation(path)
        copyValue = pptObj.slides[2]
        return_value = []
        for shape in copyValue.shapes:
            if type(shape) == Shape or type(shape) == GraphicFrame:
                return_value.append(copy.deepcopy(shape.element))
        return return_value
