from transformers import pipeline

class SentimentV2:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")  

    def predict(self, text: str):
        result = self.model(text)[0]
        score = round(result["score"], 4)

        label = result["label"]
        if score < 0.6:
            label = "UNCERTAIN"

        return {
            "version": "v2",
            "label": label,
            "score": score
        }