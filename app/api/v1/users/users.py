from http.client import HTTPException
from app.core.db.schema.users import UserBase, ResponseUsers
from app.core.db.models.users import Users
from fastapi import APIRouter, Request, Body, Depends, Path
from typing import List
from app.service.user import UserService
from app.core.db.base import *

router: APIRouter = APIRouter()


@router.post("/users", name="user 정보 추가", response_model=ResponseUsers)
async def register_users(req: UserBase, db: Session = Depends(get_db)):
    return UserService.register_users(req,db)    


@router.get("/users", name="user 정보 조회", response_model=List[ResponseUsers])
async def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)

@router.get(
    "/users/{user_name}", name="user 이름으로 user 정보 조회", response_model=ResponseUsers
)
async def get_user(user_name: str, db: Session = Depends(get_db)):
    return UserService.get_users(user_name,db)


@router.delete(
    "/users/{user_name}", name="user 이름으로 user 정보 삭제", response_model=ResponseUsers
)
async def delete_user(user_name:str,db: Session =Depends(get_db)):
    return UserService.delete_user(user_name,db)