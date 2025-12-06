from starlette.middleware.base import BaseHTTPMiddleware
import time
from utils.logger import get_logging

logger = get_logging("middleware")

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = (time.time() - start) * 1000
        logger.info(
            f"{request.method} {request.url.path} - "
            f"{response.status_code} - {duration:.2f}ms"
        )

        return response