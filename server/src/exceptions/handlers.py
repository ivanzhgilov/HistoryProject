from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .errors import ResourceNotFoundError


def register_exception_handlers(app: FastAPI) -> None:
  @app.exception_handler(ResourceNotFoundError)
  async def resource_not_found_handler(request: Request, exc: ResourceNotFoundError):
    return JSONResponse(
      status_code=404,
      content={
        "error": "Not Found",
        "resource": exc.resource,
        "id": exc.identifier,
      },
    )
