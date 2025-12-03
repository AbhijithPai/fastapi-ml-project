from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DAY 1: FastAPI is working!"}

class InputData(BaseModel):
    value: int

@app.post("/square")
def square_number(data: InputData):
    return {"Result": data.value ** 2}
