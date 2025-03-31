from sqlalchemy.orm import Session
from sqlalchemy import text

from model import LoginUserRequest, LoginUserResponse


def main(request: LoginUserRequest, db: Session) -> LoginUserResponse:
    query = text("SELECT id FROM public.user WHERE user_name = :user_name AND password = :password")
    query_params = {"user_name": request.user_name, "password": request.password}
    result = db.execute(query, query_params)
    columns = result.keys()
    rows = result.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    if len(result) == 1:
        return LoginUserResponse(result="Success")
    return LoginUserResponse(result="Failed")