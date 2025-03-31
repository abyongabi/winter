from sqlalchemy.orm import Session
from sqlalchemy import text

from model import CreateUserRequest, CreateUserResponse


def main(request: CreateUserRequest, db: Session) -> CreateUserResponse:
    query = text("INSERT INTO public.user(user_name, password) VALUES (:user_name, :password); SELECT * FROM public.user WHERE user_name = :user_name AND password = :password")
    query_params = {"user_name": request.user_name, "password": request.password}
    result = db.execute(query, query_params)
    db.commit()
    columns = result.keys()
    rows = result.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return CreateUserResponse(id=result[0].get("id"))