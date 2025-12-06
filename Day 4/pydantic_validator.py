from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class TextInput(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, v):
        if len(v.strip()) < 5:
            raise ValueError("Text too short.")
        if any(char.isdigit() for char in v):
            raise ValueError("Text cannot contain numbers.")
        return v

@app.post('/validate', response_model=TextInput)
def validate(data: TextInput):
    return {"message": f"You sent: {data.text}"}

