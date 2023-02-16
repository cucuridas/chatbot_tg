import asyncio
from rocketry import Rocketry
from app.schedulerGroup.messageGroup import group
from redbird.repos import CSVFileRepo
from rocketry.args import TaskLogger
from rocketry.log import MinimalRecord


def createScheduler() -> Rocketry:
    roketryScheduler = Rocketry(execution="async")
    roketryScheduler.include_grouper(group)

    @roketryScheduler.setup()
    def setup_app(task_logger=TaskLogger()):
        repo = CSVFileRepo(filename="./schedule_log/logs.csv", model=MinimalRecord)
        task_logger.set_repo(repo)

    return roketryScheduler


scheduler_app: Rocketry = createScheduler()
