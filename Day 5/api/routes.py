from fastapi import APIRouter
from api.schema import SentimentResponse, InputData
from inference.runner import run_sentiment

router = APIRouter()

@router.post('/sentiment', response_model=SentimentResponse)
def sentiment_analysis(data: InputData):
    return run_sentiment(data.text)