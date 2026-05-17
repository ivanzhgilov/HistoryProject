from fastapi import APIRouter

from src.schemas.common import HealthResponse
from src.schemas.epoch import Epoch, EpochListResponse
from src.schemas.source import SourcesResponse
from src.services.epoch_service import get_epoch_by_id, get_epochs_summary, get_event_by_id
from src.services.source_service import get_sources_data

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
  return HealthResponse(ok=True)


@api_router.get("/epochs", response_model=EpochListResponse)
def get_epochs() -> EpochListResponse:
  return get_epochs_summary()


@api_router.get("/epochs/{epoch_id}", response_model=Epoch)
def get_epoch(epoch_id: str) -> Epoch:
  return get_epoch_by_id(epoch_id)


@api_router.get("/events/{event_id}")
def get_event(event_id: str):
  return get_event_by_id(event_id)


@api_router.get("/sources", response_model=SourcesResponse)
def get_sources() -> SourcesResponse:
  return get_sources_data()


@api_router.get("/sources", response_model=SourcesResponse)
def get_sources() -> SourcesResponse:
  return get_sources_data()
