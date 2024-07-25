from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, constr, ValidationError
from analyzer import emotion_analyzer

app = FastAPI(
    title="Emotion Analyzer API", 
    description="API call IBM Watson NLP to analyze the emotion of a text", 
    version="2.0.0")

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v2/status")
async def read_status():
    return {"status": "OK"}


class TextRequest(BaseModel):
    text: constr(min_length=22, max_length=10000) # type: ignore
    language: constr(min_length=2, max_length=2) # type: ignore


@app.post("/api/v2/analyze")
async def analyze_text(text_request: TextRequest) -> dict:
    try:
        return emotion_analyzer(text_request.text, text_request.language)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
