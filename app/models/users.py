from datetime import datetime
from sqlalchemy import (
    Column, String, Date, DateTime, Text, func
)
from utils.common import generate_uuid
from dotenv import load_dotenv
from models import Base

load_dotenv()

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(36), default=generate_uuid, primary_key=True, unique=True)
    log_data = Column(Text)
    created_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    token = Column(Text)


