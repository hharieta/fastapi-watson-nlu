from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel, constr, ValidationError
from analyzer import emotion_analyzer

limiter = Limiter(key_func=get_remote_address)
origins = [
    "http://localhost:8000",
    "https://emotion-analyzer-ui.hharieta.lat",
]

app = FastAPI(
    title="Emotion Analyzer API", 
    description="API call IBM Watson NLP to analyze the emotion of a text", 
    version="2.0.0")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
@limiter.limit("5/minute")
async def root(request: Request):
    return {"Hello": "World"}

@app.get("/api/v2/status")
async def read_status(request: Request):
    return {"status": "OK"}

class TextRequest(BaseModel):
    text: constr(min_length=22, max_length=10000) # type: ignore
    language: constr(min_length=2, max_length=2) # type: ignore

@app.post("/api/v2/analyze")
@limiter.limit("5/minute")
async def analyze_text(request: Request, text_request: TextRequest) -> dict:
    try:
        return emotion_analyzer(text_request.text, text_request.language)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
