# Week 3 – Data & APIs: SMS Spam Classifier API

This week I exposed my SMS spam classifier as an HTTP API and built a small client:

- FastAPI service that loads and trains the model once at startup.
- `/predict` POST endpoint that accepts JSON `{ "text": "..." }` and returns `{ "label": "spam|ham", "is_spam": true|false }`.
- Python client using `requests` to call the API from the command line.

## How to run

In one terminal:

```bash
uvicorn week_3.api:app --reload
