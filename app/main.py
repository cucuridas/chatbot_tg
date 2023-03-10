import asyncio
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/home/cucuridas/chatbot_tg")
import uvicorn
from app.util.webex import WebexHook
from app.core.scheduler_server import scheduler_app
from app.core.server import app
from app.core.config import Settings


class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        scheduler_app.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run scheduler and the API"
    server = Server(
        config=uvicorn.Config(
            app,
            workers=int(Settings.SERVER_WORKER),
            loop="asyncio",
            host=Settings.SERVER_HOST,
            port=int(Settings.SERVER_PORT),
        )
    )

    async with asyncio.TaskGroup() as group:
        api = group.create_task(server.serve())
        sched = group.create_task(scheduler_app.serve())

    await asyncio.wait([sched, api])


if __name__ == "__main__":
    asyncio.run(main())


# def main():
#     WebexHook().addHook()
#     scheduler_app.serve()
#     # asyncio.run(main(scheduler_app))
#     uvicorn.run(app="core.server:app")


# if __name__ == "__main__":
#     main()
