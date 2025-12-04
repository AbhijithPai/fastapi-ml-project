from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils.logger import get_logging

logger = get_logging("regression")

model = None

def load_model():
    global model
    if model is None:
        logger.info("Loading regression model...")
        model = joblib.load("models/model.pkl")
    return model

def predict_value(value: float):
    model = load_model()
    logger.info(f"Predict request: {value}")
    return float(model.predict([[value]])[0])
