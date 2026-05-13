import pytest

from src.exceptions.errors import ResourceNotFoundError
from src.services.epoch_service import get_epoch_by_id, get_epochs_summary


def test_get_epochs_summary_returns_non_empty_list():
  result = get_epochs_summary()
  assert result.epochs, "Expected epochs list to be non-empty"
  assert all(epoch.id for epoch in result.epochs)


def test_get_epoch_by_id_returns_epoch():
  epoch = get_epoch_by_id("epoch-1")
  assert epoch.id == "epoch-1"
  assert len(epoch.events) >= 1


def test_get_epoch_by_id_raises_not_found():
  with pytest.raises(ResourceNotFoundError):
    get_epoch_by_id("unknown-epoch")
