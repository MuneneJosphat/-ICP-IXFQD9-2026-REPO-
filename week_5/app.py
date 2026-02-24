from functools import lru_cache

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

from .model import SpamClassifier
from .config import API_KEY, MODEL_DATA_PATH


MODEL_DATA_PATH = "week_2/data/SMSSpamCollection"



app = FastAPI(
    title="SMS Spam Classifier API - Week 5 (Production Ready)",
    version="0.5.0",
)


@lru_cache(maxsize=1)
def get_classifier() -> SpamClassifier:
    clf = SpamClassifier()
    clf.train(MODEL_DATA_PATH)
    return clf


class MessageIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    is_spam: bool


@app.get("/")
def root():
    return {"message": "Week 5 - Production-ready Spam API running"}


@app.post("/predict", response_model=PredictionOut)
def predict(message: MessageIn, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    clf = get_classifier()
    pred = clf.predict(message.text)
    label = "spam" if pred == 1 else "ham"
    return PredictionOut(label=label, is_spam=(pred == 1))
