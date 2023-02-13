from app.core.db.base import *
from app.core.db.schema.users import UserBase, ResponseUsers
from fastapi import APIRouter, Request, HTTPException, Body, Depends, Path
from app.core.db.models.users import Users
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


class UserService:
    def register_users(req: UserBase, db: Session = Depends(get_db)):
        user = Users(**req.dict())
        userInfo = db.query(Users).filter(Users.user_name == user.user_name).first()
        if userInfo != None:
            raise HTTPException(status_code=404, detail="User is exiet")
        else:
            db.add(user)
            db.commit()

        return user

    def get_users(db: Session = Depends(get_db)):
        users = db.query(Users).all()
        return users

    def get_user(user_name: str, db: Session = Depends(get_db)):
        userInfo = db.query(Users).filter(Users.user_name == user_name).first()
        if userInfo == None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return userInfo

    def delete_user(user_name: str, db: Session = Depends(get_db)):
        userInfo = db.query(Users).filter(Users.user_name == user_name).first()

        db.delete(userInfo)
        db.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
