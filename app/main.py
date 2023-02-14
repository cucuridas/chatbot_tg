import asyncio
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
import uvicorn
from app.util.webex import WebexHook
from app.core.scheduler_server import scheduler_app


def main():
    WebexHook().addHook()
    uvicorn.run(app="core.server:app")
    asyncio.run(main(scheduler_app))


if __name__ == "__main__":
    main()
