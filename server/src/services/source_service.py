from src.core.paths import DATA_DIR
from src.schemas.source import SourcesResponse
from src.utils.json_loader import load_json


def get_sources_data() -> SourcesResponse:
  data = load_json(DATA_DIR / "sources.json")
  return SourcesResponse(**data)
