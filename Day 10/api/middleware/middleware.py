import time
import uuid
from fastapi import Request
from core.logger import get_logger

logger =get_logger("API")

async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id =request_id

    start_time = time.time()

    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(
            "request_id = %s | ERROR | path = %s | reason = %s",
            request_id,
            request.url.path,
            str(e)
        )
        raise

    duration = round((time.time() - start_time) * 1000, 2)

    response.headers["X-Request-ID"] = request_id
    
    logger.info(
        "request_id = %s | %s %s | status = %s | time_ms = %s",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        duration
    )

    return response