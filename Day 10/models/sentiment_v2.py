from transformers import pipeline
from core.logger import get_logger

logger = get_logger("Sentimentv2")

class SentimentV2:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")  

    def predict(self, text: str, request_id: str):
        logger.info(
            "request_info = %s | prediction_starting",
            request_info
        )

        result = self.model(text)[0]
        score = round(result["score"], 4)

        label = result["label"]
        if score < 0.6:
            label = "UNCERTAIN"

        response = {
            "version": "v2",
            "label": label,
            "score": score
        }

        logger.info(
            "request_info = %s | model = v2 | prediction_completed, label = %s",
            request_info,
            response["label"]
        )

        return response