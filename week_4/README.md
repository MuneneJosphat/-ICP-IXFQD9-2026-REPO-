# Week 4 – Advanced Features: Optimization & Security

This week I profiled and secured the SMS Spam Classifier API:

## What I did
- Used `cProfile` to profile 100 predictions and identify slow spots.
- Used `lru_cache` to ensure the classifier is trained once and reused.
- Added API key authentication via request headers using `python-dotenv`.
- Stored secrets in `.env` (never committed to Git).

## How to run

Profiling:
```bash
python week_4/profiling.py
