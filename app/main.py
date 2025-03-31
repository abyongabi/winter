from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
import app.database as database

from app.model import LoginUserRequest, LoginUserResponse, CreateUserRequest, CreateUserResponse, LogUserRequest, LogUserResponse
from app.services import login_user_service, create_user_service, log_user_service

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


@app.get("/log", response_class=HTMLResponse)
async def log_weight_page():
    with open("static/log_weight.html", "r") as f:
        return f.read()


@app.get("/user/login")
async def login_user(request: Annotated[LoginUserRequest, Depends()], db: Session = Depends(database.get_db)) -> LoginUserResponse:
    result = login_user_service.main(request, db)
    if result.result == "Success":
        return RedirectResponse(url="/log")
    else:
        return HTMLResponse("<h3>Login failed, please try again.</h3>")


@app.get("/user/create")
async def create_user(request: Annotated[CreateUserRequest, Depends()], db: Session = Depends(database.get_db)) -> CreateUserResponse:
    return create_user_service.main(request, db)


@app.get("/user/log", response_class=HTMLResponse)
async def log_user(request: Annotated[LogUserRequest, Depends()], db: Session = Depends(database.get_db)) -> HTMLResponse:
    result = log_user_service.main(request, db)
    return HTMLResponse(content=f"""
        <html>
        <head>
            <title>Log Weight Result</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <h1>Weight Logged Successfully</h1>
            <p><strong>Day:</strong> {result.day}</p>
            <p><strong>Weight Difference:</strong> {result.difference} kg</p>
            <br>
            <a href="/">Back to Login</a>
        </body>
        </html>
    """)
