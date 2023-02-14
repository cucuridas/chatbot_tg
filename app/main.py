import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
import uvicorn
from app.util.webex import WebexHook


def main():
    WebexHook().addHook()
    uvicorn.run(app="core.server:app")


if __name__ == "__main__":
    main()
