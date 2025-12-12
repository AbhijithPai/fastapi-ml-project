import os
import joblib

class PredictPipeline:
    def __init__(self, model_dir = "ml/models"):
        self.model_dir = model_dir
        self.model, self.vectorizer = self._load_latest_artifacts()

    def _get_latest_version(self):
        versions = []
        for filename in os.listdir(self.model_dir):
            if filename.startswith("model_v") and filename.endswith(".pkl"):
                try:
                    v = int(filename.replace("model_v", "").replace(".pkl", ""))
                    versions.append(v)
                except:
                    pass

        return max(versions) if versions else None
    
    def _load_latest_artifacts(self):
        latest_version = self._get_latest_version()
        if latest_version is None:
            raise RuntimeError("No trained model in ml/models.")
        
        model_path = os.path.join(self.model_dir, f"model_v{latest_version}.pkl")
        vectorizer_path = os.path.join(self.model_dir, f"vectorizer_v{latest_version}.pkl")

        model = joblib.load(model_path)
        vectorizer_path = joblib.load(vectorizer_path)

    def predict(self, text: str):
        transformed = self.vectorizer.transform([text])
        prediction = self.model.predict(transformed[0])

        return {
            "input": text,
            "prediction": str(prediction)
        }
