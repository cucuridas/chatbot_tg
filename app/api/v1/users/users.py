from http.client import HTTPException
from app.core.db.schema.users import UserBase, ResponseUsers
from app.core.db.models.users import Users
from fastapi import APIRouter, Request, Body, Depends, Path
from typing import List

from app.core.db.base import *

router: APIRouter = APIRouter()


@router.post("/users", name="user 정보 추가", response_model=ResponseUsers)
async def register_users(req: UserBase, db: Session = Depends(get_db)):
    user = Users(**req.dict())
    db.add(user)
    db.commit()

    return user


@router.get("/users", name="user 정보 조회", response_model=List[ResponseUsers])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users


@router.get(
    "/users/{user_name}", name="user 이름으로 user 정보 조회", response_model=ResponseUsers
)
async def get_yser(user_name: str, db: Session = Depends(get_db)):
    userInfo = db.query(Users).filter(Users.user_name == user_name).first()
    if userInfo == None:
        raise HTTPException(status_code=404, detail="ID에 해당하는 User가 없습니다.")
    else:
        return userInfo
