import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")

from chatbot_tg.service.webhook import WebexHook

if __name__ == "__main__":
    print(WebexHook().addHook())
    # WebexHook().checkHook()
