from datetime import datetime
from sqlalchemy import (
    Column, String, Date, DateTime, Text, func
)
from utils.common import generate_uuid
from dotenv import load_dotenv
from models import Base

load_dotenv()

class Logs(Base):
    __tablename__ = 'logs'

    log_id = Column(String(36), default=generate_uuid, primary_key=True, unique=True)
    date = Column(Date)
    log_data = Column(Text)
    created_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    created_by = Column(String(36), nullable=True)

    @property
    def to_dict(self):
        return {
            "log_id": self.log_id,
            "date": str(self.date),
            "log_data": self.log_data,
            "created_at": str(self.created_at),
            "created_by": self.created_by
        }
    
