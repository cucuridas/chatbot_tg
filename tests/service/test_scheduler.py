import asyncio
import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")


from fastapi import APIRouter
from rocketry import Rocketry
from rocketry.conds import cron
from app.schedulerGroup.messageGroup import group
from redbird.repos import CSVFileRepo
from rocketry.args import TaskLogger
from rocketry.log import MinimalRecord
from app.connection.smtp import Smtp


def createScheduler() -> Rocketry:
    roketryScheduler = Rocketry(config={"task_execution": "async"})
    roketryScheduler.include_grouper(group)
    return roketryScheduler


app = Rocketry(execution="async")


@app.setup()
def setup_app(task_logger=TaskLogger()):
    repo = CSVFileRepo(filename="logs.csv", model=MinimalRecord)
    task_logger.set_repo(repo)


@app.task("every 1 minute")
async def do_things():
    return Smtp.getConnection()


# if __name__ == "__main__":
#     app.run()
async def main():
    "Launch Rocketry app (and possibly something else)"
    rocketry_task = asyncio.create_task(app.serve())
    # Start possibly other async apps
    await rocketry_task


if __name__ == "__main__":
    asyncio.run(main())
