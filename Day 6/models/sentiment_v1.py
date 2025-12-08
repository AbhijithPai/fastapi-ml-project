from transformers import pipeline

class SentimentV1:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")
    
    def predict(self, text: str):
        result = self.model(text)[0]
        return {
            "version": "v1",
            "label": result["label"],
            "score": round(result["score"], 4)
        }