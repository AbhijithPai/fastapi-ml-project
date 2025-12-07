import torch
from fastapi import FastAPI
from api.routes import router
from core.config import settings
from middleware.middleware import RequestLoggingMiddleware

app = FastAPI(title="ML API")

app.add_middleware(RequestLoggingMiddleware)
app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.ENV,
        "model_version": settings.MODEL_VERSION
    }
