from src.core.paths import DATA_DIR
from src.exceptions.errors import ResourceNotFoundError
from src.schemas.epoch import Epoch, EpochListResponse, EpochSummary, EpochEvent
from src.utils.json_loader import load_json


def get_epochs_summary() -> EpochListResponse:
  data = load_json(DATA_DIR / "epochs.json")
  raw_epochs = data.get("epochs", [])

  epochs = [
    EpochSummary(
      id=epoch.get("id", ""),
      title=epoch.get("title", ""),
      dates=epoch.get("dates", ""),
      eventsCount=len(epoch.get("events", [])),
    )
    for epoch in raw_epochs
  ]
  return EpochListResponse(epochs=epochs)


def get_epochs_summary() -> EpochListResponse:
  data = load_json(DATA_DIR / "epochs.json")
  raw_epochs = data.get("epochs", [])

  epochs = [
    EpochSummary(
      id=epoch.get("id", ""),
      title=epoch.get("title", ""),
      dates=epoch.get("dates", ""),
      eventsCount=len(epoch.get("events", [])),
    )
    for epoch in raw_epochs
  ]
  return EpochListResponse(epochs=epochs)


def get_epoch_by_id(epoch_id: str) -> Epoch:
  data = load_json(DATA_DIR / "epochs.json")
  for epoch in data.get("epochs", []):
    if epoch.get("id") == epoch_id:
      return Epoch(**epoch)
  raise ResourceNotFoundError(resource="epoch", identifier=epoch_id)


def get_event_by_id(event_id: str) -> EpochEvent:
  """
  Finds an event by its composite ID (epoch_id-index).
  """
  data = load_json(DATA_DIR / "epochs.json")

  # event_id format: epoch-id-index (e.g., epoch-1-0)
  parts = event_id.split("-")
  if len(parts) < 3:
    raise ResourceNotFoundError(resource="event", identifier=event_id)

  epoch_id = parts[0] + "-" + parts[1]
  event_index = int(parts[2]) if parts[2].isdigit() else 0

  for epoch in data.get("epochs", []):
    if epoch.get("id") == epoch_id:
      events = epoch.get("events", [])
      if 0 <= event_index < len(events):
        return EpochEvent(**events[event_index])
      break

  raise ResourceNotFoundError(resource="event", identifier=event_id)
