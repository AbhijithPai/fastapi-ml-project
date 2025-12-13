import joblib

class PredictPipeline:
    def __init__(self):
        self.model = joblib.load("models/model_v1.pkl")
        self.vectorizer = joblib.load("models/vectorizer_v1.pkl")

    def predict(self, text: str):
        vec = self.vectorizer.transform([text])
        prediction = self.model.predict(vec)[0]
        return prediction
