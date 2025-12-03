from pydantic import BaseModel
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

class TextInput(BaseModel):
    text: str


@app.post("/sentiment")

def analyze(input: TextInput):
    output = classifier(input.text)[0]
    return {
        "label": output["label"],
        "score": float(output["score"])
    }