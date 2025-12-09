from models.sentiment_v1 import SentimentV1
from models.sentiment_v2 import SentimentV2

class ModelRegistry:
    def __init__(self):
        self._models = {}
    
    def get_model(self, version: str):
        if version not in self._models:
            self._models[version] = self._load_module(version)
        return self._models[version]
    
    def _load_module(self, version: str):
        if version == "v1":
            return SentimentV1()
        elif version == "v2":
            return SentimentV2()
        else:
            return ValueError(f"Unsupported model version: {version}")
        