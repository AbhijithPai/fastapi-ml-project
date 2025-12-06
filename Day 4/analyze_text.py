from fastapi import FastAPI
from pydantic import BaseModel
from middleware import RequestLoggingMiddleware

app = FastAPI()

app.add_middleware(RequestLoggingMiddleware)

class InputData(BaseModel):
    text: str

@app.post("/analyze")
def analyze(data: InputData):
    text = data.text.lower()

    length = len(text)
    contains_abhi = "abhi" in text

    return {
        "length": length,
        "contains_abhi": contains_abhi
    }