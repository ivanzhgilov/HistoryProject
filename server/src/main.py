from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.api.routes import api_router
from src.core.logging_setup import setup_logging
from src.core.paths import FRONTEND_DIR, PAGES_DIR
from src.exceptions.handlers import register_exception_handlers
from src.middlewares.request_logging import request_logging_middleware
from src.web.routes import web_router

setup_logging()

app = FastAPI(title="Evolution Tech Thought API", version="1.0.0")
app.middleware("http")(request_logging_middleware)
register_exception_handlers(app)

templates = Jinja2Templates(directory=str(PAGES_DIR))

app.include_router(api_router)
app.include_router(web_router)

app.mount("/css", StaticFiles(directory=str(FRONTEND_DIR / "css")), name="css")
app.mount("/js", StaticFiles(directory=str(FRONTEND_DIR / "js")), name="js")
app.mount("/images", StaticFiles(directory=str(FRONTEND_DIR / "images")), name="images")
