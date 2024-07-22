from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from models.logs import Logs
from datetime import datetime
from uuid import uuid4
from sqlalchemy import func, extract, desc

async def get_logs(date, db):
    date = datetime.now() if date is None else date
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')
        year = parsed_date.year
        month = parsed_date.month
        day = parsed_date.day

        logs = db.query(Logs).filter(
            extract('year', Logs.date) == year,
            extract('month', Logs.date) == month,
            extract('day', Logs.date) == day
        ).order_by(desc(Logs.created_at)).all()

        logs_response = [log.to_dict for log in logs]

        return JSONResponse(status_code=200, content={"data": logs_response})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def add_log(log_creation_request, db):
    print("add_log called!")
    try:
        # Parse the date from the request, assuming it is in 'YYYY-MM-DD' format
        log_date = datetime.strptime(log_creation_request.date, '%Y-%m-%d').date()

        # Create a new log entry
        new_log = Logs(
            log_id=str(uuid4()),  # Generate a new UUID for the log_id
            date=log_creation_request.date,
            log_data=log_creation_request.log_data,
            created_at=func.now(),
            created_by="system"  # Replace with actual user info in a real application
        )

        # Add and commit the new log to the database
        db.add(new_log)
        db.commit()
        db.refresh(new_log)

        return JSONResponse(status_code=201, content=new_log.to_dict)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

async def update_log(log_id, log_update_request, db):
    print("update_log called!")
    try:
        # Retrieve the log entry from the database
        log_entry = db.query(Logs).filter(Logs.log_id == log_id).first()

        if log_entry is None:
            raise HTTPException(status_code=404, detail="Log entry not found")

        # Update the log entry fields
        if log_update_request.date:
            log_entry.date = datetime.strptime(log_update_request.date, '%Y-%m-%d').date()
        if log_update_request.log_data:
            log_entry.log_data = log_update_request.log_data

        log_entry.updated_at = func.now()
        log_entry.updated_by = "system"  # Replace with actual user info in a real application

        # Commit the changes to the database
        db.commit()
        db.refresh(log_entry)

        return JSONResponse(status_code=200, content=log_entry.to_dict)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


