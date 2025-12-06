from fastapi import FastAPI
from pydantic import BaseModel
from models.regression import predict_with_version

app = FastAPI(title="Model Versioning API")

class NumberInput(BaseModel):
    value: float

class PredictionResponse(BaseModel):
    version: str
    input: float
    prediction: float


@app.post("/predict/v1", response_model=PredictionResponse)
def predict_v1(data: NumberInput):
    prediction = predict_with_version(data.value, version="v1")
    return PredictionResponse(
        version="v1",
        input=data.value,
        prediction=prediction
    )


@app.post("/predict/v2", response_model=PredictionResponse)
def predict_v2(data: NumberInput):
    prediction = predict_with_version(data.value, version="v2")
    return PredictionResponse(
        version="v2",
        input=data.value,
        prediction=prediction
    )
