from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import traceback

from src.core.paths import FRONTEND_DIR, PAGES_DIR, ROOT_DIR
from src.services.epoch_service import get_event_by_id, get_epoch_by_id
from src.schemas.epoch import EpochEvent, Epoch

web_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory=str(PAGES_DIR))


def _safe_page_name(name: str) -> bool:
  return bool(name) and all(ch.isalnum() or ch in ("-", "_") for ch in name)


@web_router.get("/robots.txt")
def robots():
  return FileResponse(str(ROOT_DIR / "robots.txt"))


@web_router.get("/favicon.ico")
def favicon():
  return FileResponse(str(FRONTEND_DIR / "images" / "favicon.ico"))


@web_router.get("/sitemap.xml")
def sitemap():
  return FileResponse(str(ROOT_DIR / "sitemap.xml"))


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
def page_clean(request: Request, page: str):
  if not _safe_page_name(page):
    return JSONResponse({"error": "Not Found"}, status_code=404)

  # Special case for event details
  if page.startswith("event-"):
    event_id = page[6:] # remove "event-"
    try:
      event = get_event_by_id(event_id)

      # Find epoch for this event to get the title and list of events
      parts = event_id.split("-")
      if len(parts) >= 3:
        epoch_id = parts[0] + "-" + parts[1]
        epoch = get_epoch_by_id(epoch_id)

        # Calculate event index for prev/next buttons
        # get_epoch_by_id returns the full epoch object including events list
        events = epoch.events
        event_index = -1
        for idx, e in enumerate(events):
            # events in JSON might be simple dicts, we need to match by content or assume order
            # The JS code assumes the index is the last part of the event-id
            # e.g. event-epoch-1-0 -> index 0
            pass

        # Actually, the event_id is composite: epoch-id-index
        # We can just use the index from the ID
        try:
            event_index = int(parts[2])
        except (ValueError, IndexError):
            event_index = -1

        return templates.TemplateResponse(
            request=request,
            name="event.html",
            context={
                "event": event.model_dump(),
                "epoch": epoch.model_dump(),
                "event_index": event_index,
                "total_events": len(events)
            }
        )

      return templates.TemplateResponse(
          request=request,
          name="event.html",
          context={
              "event": event.model_dump(),
              "epoch": None,
              "event_index": -1,
              "total_events": 0
          }
      )
    except Exception as e:
      # Удаляем отладочный вывод, чтобы вернуть код в чистое состояние
      return JSONResponse({"error": str(e)}, status_code=404)

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


@web_router.get("/favicon.ico")
def favicon():
  return FileResponse(str(FRONTEND_DIR / "images" / "favicon.ico"))


@web_router.get("/sitemap.xml")
def sitemap():
  return FileResponse(str(ROOT_DIR / "sitemap.xml"))
