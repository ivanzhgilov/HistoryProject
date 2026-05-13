from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse

from src.core.paths import FRONTEND_DIR, PAGES_DIR, ROOT_DIR

web_router = APIRouter(include_in_schema=False)


def _safe_page_name(name: str) -> bool:
  return bool(name) and all(ch.isalnum() or ch in ("-", "_") for ch in name)


@web_router.get("/")
def home():
  return FileResponse(str(FRONTEND_DIR / "index.html"))


@web_router.get("/index.html")
def home_html():
  return RedirectResponse(url="/", status_code=308)


@web_router.get("/pages/{page}")
def legacy_pages_clean(page: str):
  if not _safe_page_name(page):
    return JSONResponse({"error": "Not Found"}, status_code=404)
  return RedirectResponse(url=f"/{page}", status_code=308)


@web_router.get("/{page}")
def page_clean(page: str):
  if not _safe_page_name(page):
    return JSONResponse({"error": "Not Found"}, status_code=404)
  file_path = PAGES_DIR / f"{page}.html"
  if not file_path.exists():
    return JSONResponse({"error": "Not Found"}, status_code=404)
  return FileResponse(str(file_path))


@web_router.get("/pages/{page}.html")
def pages_html(page: str):
  if not _safe_page_name(page):
    return JSONResponse({"error": "Not Found"}, status_code=404)
  return RedirectResponse(url=f"/{page}", status_code=308)


@web_router.get("/{page}.html")
def legacy_root_html(page: str):
  if not _safe_page_name(page):
    return JSONResponse({"error": "Not Found"}, status_code=404)
  if page == "index":
    return RedirectResponse(url="/", status_code=308)
  return RedirectResponse(url=f"/{page}", status_code=308)


@web_router.get("/robots.txt")
def robots():
  return FileResponse(str(ROOT_DIR / "robots.txt"))


@web_router.get("/sitemap.xml")
def sitemap():
  return FileResponse(str(ROOT_DIR / "sitemap.xml"))
