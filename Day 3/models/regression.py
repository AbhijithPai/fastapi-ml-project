import os
import joblib
from utils.logger import get_logging 

BASE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE, "model_files")

_loaded = {}  # cache loaded models

def load_model(version: str = "v1"):
    key = version
    if key in _loaded:
        return _loaded[key]

    path = os.path.join(MODEL_DIR, f"model_{version}.pkl")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
    model = joblib.load(path)
    _loaded[key] = model
    return model

def predict_with_version(value: float, version: str = "v1"):
    model = load_model(version)
    # model expects 2D
    pred = model.predict([[value]])[0]
    return float(pred)
