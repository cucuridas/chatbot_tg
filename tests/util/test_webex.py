from io import BytesIO, StringIO
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
from app.util.webex import Messages
from pptx import Presentation

url = "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL0NPTlRFTlQvMTkwZmU2NDAtYWU4MS0xMWVkLWJjMzItMmRmYTZmYTU4NTNiLzA"
response = Messages().downloadFile(url)
content = response.content
print(type(content))


presentation = Presentation("/Users/cucuridas/Desktop/chatbot_tg/test.pptx")
output = BytesIO(content)
presentation.save(output)
output.read()
