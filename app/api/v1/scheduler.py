from app.core.server import scheduler
from fastapi import APIRouter


router: APIRouter = APIRouter()
session = scheduler.session


@router.post("/shcheduler/shut_down")
async def shut_down_session():
    "Shut down the scheduler"
    session.shut_down()


@router.post("/shcheduler/{task_name}/run", name="task 이름을 입력받아 실행 시키는 API")
async def runScheduler(task_name: str):
    task = session[task_name]
    task.force_run = True
    return "Success"


@router.get("/shcheduler")
async def read_tasks():
    return list(session.tasks)


@router.get("shcheduler/logs")
async def read_logs():
    repo = session.get_repo()
    return repo.filter_by().all()
