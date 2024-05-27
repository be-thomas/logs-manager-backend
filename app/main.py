import sys
import os
from models import Base, engine
from models import logs, users

if __name__ == '__main__':
    # Add the current project directory to sys.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from app.routes.initiate_routes import InitiateRouters
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import logging

load_dotenv()

# Initiate the FastAPI
app = FastAPI(
    title=os.getenv("PROJECT_NAME"),
    version=os.getenv("PROJECT_VERSION"),
    swagger_ui_parameters={"syntaxHighlight.theme": "arta-dark"},
)


# CORS Middleware Defined
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

# Step 1: Create a logger instance
logger = logging.getLogger(__name__)

#         We can handle all exceptions in one place, using the 'Exception' superclass.
@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    logger.exception(exc)
    return JSONResponse(status_code=500, content={"error": str(exc)})


# Migrate DB and run seeders
# Base.metadata.drop_all(engine)
# logger.info("database is cleaned...")
# Base.metadata.create_all(engine)
# logger.info("database is set...")


InitiateRouters(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", host="127.0.0.1", port=int(os.getenv("APP_PORT", "8080")), reload=False
    )

