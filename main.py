from typing import Optional, Annotated
from fastapi import FastAPI, Depends

from model import LoginRequest, LoginResponse
from services import login_service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/login")
def login(request: Annotated[LoginRequest, Depends()]) -> LoginResponse:
    return login_service.main(request)