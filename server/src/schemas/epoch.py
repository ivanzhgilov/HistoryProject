from pydantic import BaseModel


class EpochEvent(BaseModel):
  year: str
  title: str
  people: str
  description: str


class Epoch(BaseModel):
  id: str
  title: str
  short_title: str
  dates: str
  events: list[EpochEvent]


class EpochSummary(BaseModel):
  id: str
  title: str
  dates: str
  eventsCount: int


class EpochListResponse(BaseModel):
  epochs: list[EpochSummary]
