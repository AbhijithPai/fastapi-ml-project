from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Sentiment API")
app.include_router(router)
