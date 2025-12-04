from transformers import pipeline
from utils.logger import get_logging

logger = get_logging("setiment")

classifier = None

def load_classifier():
    global classifier
    if classifier is None:
        logger.info("Loading sentiment model...")
        classifier = pipeline("sentiment-analysis")
    return classifier

def analyse(text: str):
    classifier = load_classifier()
    logger.info(f"Sentiment request: {text}")
    result = classifier(text)[0]
    return {"label": result["label"], "score": float(result["score"])}