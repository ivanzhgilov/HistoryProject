import os

from dotenv import load_dotenv

from .paths import SERVER_DIR

load_dotenv(SERVER_DIR / ".env")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
