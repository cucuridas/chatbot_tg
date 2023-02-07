import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")
from app.service.webex import WebexHook, Messages

if __name__ == "__main__":
    # print(WebexHook().addHook())
    # WebexHook().checkHook()

    # Messages().getMessage(
    #     "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvZDJmZmJkMzAtYTVlNi0xMWVkLWJmM2YtMzM4MWI5NTI4ZDFi"
    # )
    Messages().postMessage(
        "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjlhNjU3YjAtYzliNy0xMWVjLTgzNGMtODU3MjZiZTViYWFi",
        "이렇게하면됩니까?",
    )
