from sqlalchemy.orm import Session
from sqlalchemy import text

from app.model import LogUserRequest, LogUserResponse


def main(request: LogUserRequest, db: Session):
    query = text("SELECT * FROM public.log WHERE user_id = :user_id ORDER BY date DESC LIMIT 1")
    query_params = {"user_id": request.user_id}
    result = db.execute(query, query_params)
    columns = result.keys()
    rows = result.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    if result:
        result = result[0]
        day = result["day"] + 1
        difference = request.weight - result["weight"]
    else:
        day = 1
        difference = 0
    query = text("INSERT INTO public.log(user_id, day, weight, difference, date) VALUES (:user_id, :day, :weight, :difference, CURRENT_TIMESTAMP AT TIME ZONE 'Australia/Sydney');")
    query_params = {"user_id": request.user_id, "day": day, "weight": request.weight, "difference": difference}
    db.execute(query, query_params)
    db.commit()
    return LogUserResponse(day=day, difference=difference)