from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Query
from schemas.logs_schemas import LogsResponse, LogCreationRequest, LogCreationResponse
from starlette import status
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import get_db
from controllers import logs_controller

router = APIRouter(prefix="/logs", tags=["Test"])


@router.get("/get_logs", response_model=LogsResponse, status_code=status.HTTP_200_OK)
async def get_logs(
    date: str = Query(default=None),
    db: Session = Depends(get_db)
):
    return await logs_controller.get_logs(date, db)



@router.post("/add_log", response_model=LogCreationResponse, status_code=status.HTTP_201_CREATED)
async def add_log(
    log_creation_request: LogCreationRequest,
    db: Session = Depends(get_db)
):
    return await logs_controller.add_log(log_creation_request, db)


@router.patch("/update_log/{log_id}", response_model=LogCreationResponse, status_code=status.HTTP_200_OK)
async def update_log(
    log_id: str,
    log_update_request: LogCreationRequest,
    db: Session = Depends(get_db)
):
    return await logs_controller.update_log(log_id, log_update_request, db)

