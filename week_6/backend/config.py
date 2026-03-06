from pathlib import Path

# BASE_DIR should be the repo root
BASE_DIR = Path(__file__).resolve().parents[2]

API_KEY = "mysecretkey123"

# Correct path to week_2/data/SMSSpamCollection from repo root
MODEL_DATA_PATH = str(BASE_DIR / "week_2" / "data" / "SMSSpamCollection")

# Put spam.db inside backend folder
BACKEND_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BACKEND_DIR / 'spam.db'}"
