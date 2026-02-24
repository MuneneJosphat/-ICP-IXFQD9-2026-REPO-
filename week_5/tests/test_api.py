from week_5.model import SpamClassifier
from week_5.config import MODEL_DATA_PATH

from fastapi.testclient import TestClient

from week_5.app import app
from week_5.config import API_KEY

client = TestClient(app)


def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Week 5" in resp.json()["message"]


def test_predict_with_valid_key():
    payload = {"text": "Free entry in 2 a weekly comp to win cash!"}
    headers = {"x-api-key": API_KEY}

    resp = client.post("/predict", json=payload, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["label"] in ("spam", "ham")
    assert isinstance(data["is_spam"], bool)


def test_predict_with_invalid_key():
    payload = {"text": "Hello, how are you?"}
    headers = {"x-api-key": "wrong"}

    resp = client.post("/predict", json=payload, headers=headers)
    assert resp.status_code == 401
