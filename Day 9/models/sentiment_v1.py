from transformers import pipeline
from core.logger import get_logger
from middleware.middleware import log_requests

logger = get_logger("SentimentV1")

class SentimentV1:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")
    
    def predict(self, text: str, request_id: str):
        logger.info(
            "request_id = %s | model = v1 | prediction_started",
            request_id,
        )

        result = self.model(text)[0]

        response = {
            "version": "v1",
            "label": result["label"],
            "score": round(result["score"], 4)
        }

        logger.info(
            "request_id = %s | model=v1 | prediction_completed, label = %s",
            request_id,
            response["label"]
        )

        return response