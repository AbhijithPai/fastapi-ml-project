from fastapi import FastAPI
from api.routes import router
from middleware.middleware import log_requests

app = FastAPI(title = "Sentiment Analaysis")

@app.middleware("http")
async def request_logger(request, call_next):
    return await log_requests(request, call_next)

app.include_router(router)