from pydantic import BaseModel

class InputData(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    value: float