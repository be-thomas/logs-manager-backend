import logging
from urllib import parse
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from loguru import logger
import os
import sys
load_dotenv()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{parse.quote(os.getenv('DB_PASSWORD'))}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    except Exception as error:
        error_message = "Database connection error: " + str(error)
        logger.exception("get_db:: error - " + error_message)
        return JSONResponse(content={"message": error_message}, status_code=500)
    finally:
        db.close()


def get_db_instance():
    try:
        db = sessionLocal()
        return db
    except Exception as error:
        error_message = "Database connection error: " + str(error)
        logger.exception("get_db_instance:: error - " + error_message)
        return JSONResponse(content={"message": error_message}, status_code=500)

