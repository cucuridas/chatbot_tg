from io import BytesIO, StringIO
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.util.webex import Messages
from pptx import Presentation

url = "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL0NPTlRFTlQvMTkwZmU2NDAtYWU4MS0xMWVkLWJjMzItMmRmYTZmYTU4NTNiLzA"
# response = Messages().downloadFile(url)
# content = response.content

# with open("tes1t.pptx", "wb") as f:
#     f.write(content)


# content = Messages().downloadFile(url)
# Messages.saveFiletoPptx(content, "최충은")
