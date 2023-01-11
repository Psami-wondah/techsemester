import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")


DB_ENGINE = os.getenv("DB_ENGINE", "django.db.backends.sqlite3")
POSTGRES_DB = os.getenv("POSTGRES_DB", BASE_DIR / "db.sqlite3")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


API_DOCUMENTATION_URL = os.getenv("API_DOCUMENTATION_URL")
