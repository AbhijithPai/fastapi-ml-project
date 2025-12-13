from fastapi import FastAPI
from api.routes import router
from api.middleware.logging import logging_middleware

app = FastAPI(title="Sentiment API")
app.include_router(router)
app.middleware("http")(logging_middleware)

