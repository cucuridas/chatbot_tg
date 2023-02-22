import asyncio
from rocketry import Rocketry
from app.schedulerGroup.messageGroup import group
from redbird.repos import CSVFileRepo
from rocketry.args import TaskLogger
from rocketry.log import MinimalRecord


"""
scheduler 서버를 생성하는 파이썬 파일입니다
"""


def createScheduler() -> Rocketry:
    """
    roketry를 통해 scheduler 서버를 생성하는 함수입니다

    Returns:
        roketryScheduler: Rocketry

    """
    roketryScheduler = Rocketry(execution="async")
    roketryScheduler.include_grouper(group)

    @roketryScheduler.setup()
    def setup_app(task_logger=TaskLogger()):
        repo = CSVFileRepo(filename="./schedule_log/logs.csv", model=MinimalRecord)
        task_logger.set_repo(repo)

    return roketryScheduler


scheduler_app: Rocketry = createScheduler()
