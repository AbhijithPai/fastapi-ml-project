from fastapi import APIRouter, Query, Request
from api.schema import SentimentResponse, InputData
from core.model_registry import ModelRegistry

router = APIRouter()
registry = ModelRegistry()

@router.post('/predict', response_model=SentimentResponse)
def predict(request_data: InputData, request : Request, version: str = Query("v1")):
    model = registry.get_model(version)
    return model.predict(request_data.text, request.state.request_id)