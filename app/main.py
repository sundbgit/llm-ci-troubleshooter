# Api layer

from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_log

app = FastAPI()

class LogRequest(BaseModel):
    log: str

@app.post("/analyze_ci_log/")
def analyze(request: LogRequest):

    result = analyze_log(request.log)

    return {
        "suggested_fix": result
    }


