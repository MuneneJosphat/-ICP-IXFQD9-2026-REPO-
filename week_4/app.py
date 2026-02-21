import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from functools import lru_cache
from week_4.model import SpamClassifier

# Load .env
load_dotenv("week_4/.env")
API_KEY = os.getenv("API_KEY", "defaultkey")

app = FastAPI(title="SMS Spam Classifier API - Week 4 (Secured + Optimized)")

# Train once at startup, cache the classifier
@lru_cache(maxsize=1)
def get_classifier():
    clf = SpamClassifier()
    clf.train("week_2/data/SMSSpamCollection")
    return clf


class MessageIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    is_spam: bool


@app.get("/")
def root():
    return {"message": "Week 4 - Secured Spam API running"}


@app.post("/predict", response_model=PredictionOut)
def predict(message: MessageIn, x_api_key: str = Header(...)):
    # Security: validate API key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    clf = get_classifier()
    pred = clf.predict(message.text)
    label = "spam" if pred == 1 else "ham"
    return PredictionOut(label=label, is_spam=(pred == 1))
