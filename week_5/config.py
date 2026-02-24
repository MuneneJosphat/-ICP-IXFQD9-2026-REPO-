from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from repo root
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY", "defaultkey")
ENV = os.getenv("ENV", "local")

MODEL_DATA_PATH = os.getenv(
    "MODEL_DATA_PATH",
    str(BASE_DIR / "week_2" / "data" / "SMSSpamCollection"),
)

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
