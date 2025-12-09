from pydantic import BaseModel

class InputData(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    version: str
    label: str
    score: float