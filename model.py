from pydantic import BaseModel
from typing import Literal


class LoginRequest(BaseModel):
    user_name: str
    password: str


class LoginResponse(BaseModel):
    result: Literal['Success', 'Failed']
