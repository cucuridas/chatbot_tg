from app.core.db.base import *
from app.core.db.schema.team import ReqTeamInfoSchema
from fastapi import HTTPException, Depends
from app.core.db.models.team import TeamModel
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


class TeamService:
    def registTeam(req: ReqTeamInfoSchema, db: Session = Depends(get_db)):
        team = TeamModel(**req.dict())
        teamInfo = db.query(TeamModel).filter(TeamModel.team_name == team.team_name).first()
        if teamInfo != None:
            raise HTTPException(status_code=404, detail="Team is exiet")
        else:
            db.add(team)
            db.commit()
        return req

    def deleteTeam(team_name: str, db: Session = Depends(get_db)):
        teamInfo = db.query(TeamModel).filter(TeamModel.team_name == team_name).first()

        db.delete(teamInfo)
        db.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

    def getTeams(db: Session = Depends(get_db)):
        teams = db.query(TeamModel).all()
        return teams

    def updateTeam(req: ReqTeamInfoSchema, team_name, db):
        # teamInfo = TeamModel(*req.dict())
        db.query(TeamModel).filter(TeamModel.team_name == team_name).update(req.dict())
        db.commit()
        return req
