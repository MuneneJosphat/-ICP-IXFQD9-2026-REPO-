# Week 2 – Core Concepts: SMS Spam Classifier (CLI)

This week I implemented a simple command-line spam classifier in Python:

- Uses the SMS Spam Collection corpus (ham/spam) as training data.
- Converts text messages to TF-IDF features.
- Trains a Logistic Regression model to classify messages as spam (1) or ham (0).
- Provides a CLI where you can type a message and see the prediction.

## How to run

From the repo root, with the virtual environment activated:

```bash
python week_2/app.py
