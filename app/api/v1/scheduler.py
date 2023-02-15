from app.core.scheduler_server import scheduler_app
from fastapi import APIRouter


router: APIRouter = APIRouter(tags=["Scheduler"])
session = scheduler_app.session


@router.post("/shcheduler/shut_down")
async def shut_down_session():
    "Shut down the scheduler"
    session.shut_down()


@router.post("/shcheduler/{task_name}/run", name="task 이름을 입력받아 예약 시키는 API")
async def runScheduler(task_name: str):
    task = session[task_name]
    task.force_run = True
    return "Success"


@router.post("/shcheduler/{task_name}/stop", name="task 이름을 입력받아 예약해제 시키는 API")
async def stopScheduler(task_name: str):
    task = session[task_name]
    task.force_run = False
    return "Success"


@router.get("/shcheduler")
async def read_tasks():
    return list(session.tasks)


@router.get("shcheduler/logs")
async def read_logs():
    repo = session.get_repo()
    return repo.filter_by().all()
