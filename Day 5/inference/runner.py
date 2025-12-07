from transformers import pipeline
from core.logger import get_logger

logger = get_logger("sentiment")

classifier = None

def load_classifier():
    global classifier
    if classifier is None:
        logger.info("Loading sentiment model. . .")
        classifier = pipeline("sentiment-analysis")
    return classifier

def run_sentiment(text: str):
    classifier = load_classifier()
    logger.info(f"Sentiment request: {text}")
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "value": float(result["score"])
    }