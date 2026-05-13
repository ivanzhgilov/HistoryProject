from src.core.paths import DATA_DIR
from src.exceptions.errors import ResourceNotFoundError
from src.schemas.epoch import Epoch, EpochListResponse, EpochSummary
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


def get_epoch_by_id(epoch_id: str) -> Epoch:
  data = load_json(DATA_DIR / "epochs.json")
  for epoch in data.get("epochs", []):
    if epoch.get("id") == epoch_id:
      return Epoch(**epoch)
  raise ResourceNotFoundError(resource="epoch", identifier=epoch_id)
