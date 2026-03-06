
from functools import lru_cache

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

from .model import SpamClassifier
from .config import API_KEY, MODEL_DATA_PATH
from .db import init_db, save_prediction, get_recent_predictions
from .schemas import MessageIn, PredictionOut, PredictionLog


app = FastAPI(
    title="SMS Spam Classifier Capstone",
    version="0.6.0",
)

# CORS so React frontend can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache(maxsize=1)
def get_classifier() -> SpamClassifier:
    clf = SpamClassifier()
    clf.train(MODEL_DATA_PATH)
    return clf


@app.on_event("startup")
def on_startup():
    init_db()
    # model lazy-loads on first predict via get_classifier()


@app.get("/")
def root():
    return {"message": "Capstone SMS Spam API running"}


@app.post("/predict", response_model=PredictionOut)
def predict(message: MessageIn, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    clf = get_classifier()
    pred = clf.predict(message.text)
    label = "spam" if pred == 1 else "ham"
    is_spam = pred == 1

    # log to DB
    save_prediction(text=message.text, label=label, is_spam=is_spam)

    return PredictionOut(label=label, is_spam=is_spam)


@app.get("/predictions", response_model=list[PredictionLog])
def list_predictions(limit: int = 50, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    records = get_recent_predictions(limit=limit)
    return records
