import time
from fastapi import Request
from app.utils.logger import get_logging

logger = get_logging("request-logging")

async def logging_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    logger.info({
        "path": request.url.path,
        "method": request.method,
        "latency": duration
    })

    return response