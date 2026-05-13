from pydantic import BaseModel


class ArchiveLink(BaseModel):
  title: str
  url: str


class SourcesResponse(BaseModel):
  sources: list[str]
  archives: list[ArchiveLink]
