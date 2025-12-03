from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DAY 1: FastAPI is working!"}

class InputData(BaseModel):
    value: int

@app.post("/square")
def square_number(data: InputData):
    return {"Result": data.value ** 2}

model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: InputData):
    print("Received input:", data.value)
    prediction = model.predict([[data.value]])[0]
    print("Prediction:", prediction)
    return {"prediction": float(prediction)}
