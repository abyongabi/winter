from pydantic import BaseModel
from typing import Literal


class LoginUserRequest(BaseModel):
    user_name: str
    password: str


class LoginUserResponse(BaseModel):
    result: Literal['Success', 'Failed']


class CreateUserRequest(BaseModel):
    user_name: str
    password: str


class CreateUserResponse(BaseModel):
    id: int
