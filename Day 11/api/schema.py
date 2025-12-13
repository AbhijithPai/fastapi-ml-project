from pydantic import BaseModel

class InputData(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str