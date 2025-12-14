from fastapi import FastAPI
from app.api.routes import router
from app.middleware.logging import logging_middleware

app = FastAPI(title = "LLMOps API")

app.middleware("http")(logging_middleware)
app.include_router(router)

@app.get("/health")
def health():
    return {
        "status": "OK"
    }

@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }