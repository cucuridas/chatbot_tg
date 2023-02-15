from http.client import HTTPException
from app.core.db.schema.team import ReqTeamInfoSchema, ResTeamInfoSchema
from fastapi import APIRouter, Request, Body, Depends, Path
from typing import List
from app.service.team import TeamService
from app.core.db.base import *


router: APIRouter = APIRouter(tags=["team"])


@router.post("/team", name="team 정보 추가", response_model=ReqTeamInfoSchema)
async def registTeam(req: ReqTeamInfoSchema, db: Session = Depends(get_db)):
    return TeamService.registTeam(req, db)


@router.delete("/team/{team_name}", name="team 이름으로 team 정보 삭제")
async def delete_user(team_name: str, db: Session = Depends(get_db)):
    return TeamService.deleteTeam(team_name, db)


@router.post("/team/{team_name}/update", name="team 이름으로 정보 수정", response_model=ReqTeamInfoSchema)
async def updateTeam(req: ReqTeamInfoSchema, team_name: str, db: Session = Depends(get_db)):
    return TeamService.updateTeam(req, team_name, db)


@router.get("/teams", name="team 정보 조회", response_model=List[ResTeamInfoSchema])
async def getTeam(db: Session = Depends(get_db)):
    return TeamService.getTeams(db)
