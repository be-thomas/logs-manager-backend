from typing import List
from pydantic import BaseModel, Field

class Log(BaseModel):
    log_id: str = Field(None, description="Log ID")
    date: str = Field(None, description="Log Date")
    log_data: str = Field(None, description="Log Contents")
    created_at: str = Field(None, description="The DateTime, when this log was added to the database")
    created_by: str = Field(None, description="Description about who added the log to the database")

class LogsResponse(BaseModel):
    data: List[Log]


class LogCreationRequest(BaseModel):
    date: str = Field(None, description="Log Date")
    log_data: str = Field(None, description="Log Contents")


class LogCreationResponse(Log):
    pass

