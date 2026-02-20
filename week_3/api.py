from fastapi import FastAPI
from pydantic import BaseModel
from week_3.model import SpamClassifier

app = FastAPI(title="SMS Spam Classifier API")

# Load and train once at startup
clf = SpamClassifier()
clf.train("week_2/data/SMSSpamCollection")


class MessageIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    is_spam: bool


@app.get("/")
def root():
    return {"message": "SMS Spam Classifier API is running"}


@app.post("/predict", response_model=PredictionOut)
def predict(message: MessageIn):
    pred = clf.predict(message.text)
    label = "spam" if pred == 1 else "ham"
    return PredictionOut(label=label, is_spam=(pred == 1))
