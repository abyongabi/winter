from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database

from model import LoginUserRequest, LoginUserResponse, CreateUserRequest, CreateUserResponse
from services import login_user_service, create_user_service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/login")
def login_user(request: Annotated[LoginUserRequest, Depends()], db: Session = Depends(database.get_db)) -> LoginUserResponse:
    return login_user_service.main(request, db)


@app.get("/user/create")
def create_user(request: Annotated[CreateUserRequest, Depends()], db: Session = Depends(database.get_db)) -> CreateUserResponse:
    return create_user_service.main(request, db)