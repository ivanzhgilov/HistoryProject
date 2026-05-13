from pathlib import Path

SERVER_DIR = Path(__file__).resolve().parents[2]
ROOT_DIR = SERVER_DIR.parents[0]
FRONTEND_DIR = ROOT_DIR / "frontend"
PAGES_DIR = FRONTEND_DIR / "pages"
DATA_DIR = SERVER_DIR / "data"
LOG_DIR = SERVER_DIR / "logs"
