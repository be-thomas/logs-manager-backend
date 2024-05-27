import uuid
from loguru import logger

def generate_uuid():
    """**Summary:**
    Generate and return a UUID (Universally Unique Identifier).
    """
    try:
        return str(uuid.uuid4())
    except Exception as error:
        logger.exception("generate_uuid:: error - " + str(error))
        raise error

