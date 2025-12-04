from fastapi import FastAPI
from pydantic import BaseModel
from models.regression import predict_value
from models.sentimentanalysis import analyse

app = FastAPI(title = "MLops Project Day 2")

class NumberInput(BaseModel):
    value: float

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: NumberInput):
    return {"prediction": predict_value(input.value)}

@app.post("/sentiment")
def sentiment(input: TextInput):
    return analyse(input.text)