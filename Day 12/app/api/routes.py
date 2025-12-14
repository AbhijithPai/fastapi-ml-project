from fastapi import APIRouter
from app.llm.inference import run_inference

router = APIRouter()

@router.post('/analyze')
def analyze(text: str):
    result = run_inference(text)
    return {
        "status": "success",
        "result": result
    }