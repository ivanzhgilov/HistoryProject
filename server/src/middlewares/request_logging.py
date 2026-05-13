import logging
from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("server")


async def request_logging_middleware(request: Request, call_next):
  start = datetime.now()
  try:
    response = await call_next(request)
    duration_ms = int((datetime.now() - start).total_seconds() * 1000)
    logger.info("%s %s -> %s (%sms)", request.method, request.url.path, response.status_code, duration_ms)
    return response
  except Exception:
    duration_ms = int((datetime.now() - start).total_seconds() * 1000)
    logger.exception("%s %s -> 500 (%sms)", request.method, request.url.path, duration_ms)
    return JSONResponse({"error": "Internal Server Error"}, status_code=500)
