from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
import app.database as database

from app.model import LoginUserRequest, LoginUserResponse, CreateUserRequest, CreateUserResponse
from app.services import login_user_service, create_user_service

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/login.html", "r") as f:
        return f.read()


@app.get("/create", response_class=HTMLResponse)
async def create_user_page():
    with open("static/create_user.html", "r") as f:
        return f.read()


@app.get("/user/login")
async def login_user(request: Annotated[LoginUserRequest, Depends()], db: Session = Depends(database.get_db)) -> LoginUserResponse:
    result = login_user_service.main(request, db)
    if result.result == "Success":
        return RedirectResponse(url="/create")
    else:
        return HTMLResponse("Login failed, please try again.")


@app.get("/user/create")
async def create_user(request: Annotated[CreateUserRequest, Depends()], db: Session = Depends(database.get_db)) -> CreateUserResponse:
    return create_user_service.main(request, db)