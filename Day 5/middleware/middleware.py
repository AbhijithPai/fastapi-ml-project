from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time
from core.logger import get_logger

logger = get_logger("middleware")

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.time()

        response = await call_next(request)

        duration_ms = (time.time() - start_time) * 1000

        logger.info(
            f"{request.method} {request.url.path} - "
            f"{response.status_code} - {duration_ms:.2f}ms"
        )

        return response
