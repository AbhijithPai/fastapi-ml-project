from fastapi import APIRouter
from api.schema import InputData, SentimentResponse
from inference.predict import PredictPipeline

router = APIRouter()
predictor = PredictPipeline()

@router.post("/predict", response_model=SentimentResponse)
def predict(payload: InputData):
    result = predictor.predict(payload.text)
    return {"sentiment": result}
