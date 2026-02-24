# Week 5 – Production Readiness: Deployment & Testing

This week takes the **SMS Spam Classifier API** from a local optimized prototype (Week 4) to a more **production-ready** service with clean configuration, automated tests, and containerized deployment.[file:21]

---

## 1. Project Overview

- **Goal:** Deploy the SMS spam classifier API and add proper testing.[file:21]  
- **Stack:** FastAPI, scikit-learn, Pytest, Docker, python-dotenv.[file:21]  
- **Data:** Uses the same `SMSSpamCollection` dataset from `week_2/data/SMSSpamCollection`.[file:21]  

The API exposes a `/predict` endpoint that takes an SMS text and returns whether it is spam or ham.  
Security is handled via an **API key** in the `x-api-key` request header (same idea as Week 4).

---

## 2. Folder Structure (Week 5)

From the repo root:

```bash
.
├── week_2/
│   └── data/
│       └── SMSSpamCollection
├── week_4/
│   ├── models.py
│   ├── app.py
│   ├── profiling.py
│   └── .env
└── week_5/
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .env.example
    ├── README.md
    └── tests/
        ├── __init__.py
        ├── test_model.py
        └── test_api.py
