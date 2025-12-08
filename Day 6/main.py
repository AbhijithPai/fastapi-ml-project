from fastapi import FastAPI
from api.routes import router

app = FastAPI(title = "Sentiment Analaysis")

app.include_router(router)