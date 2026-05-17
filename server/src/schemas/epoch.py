from pydantic import BaseModel


from pydantic import BaseModel


class SectionImage(BaseModel):
  url: str
  caption: str | None = None


class EventSection(BaseModel):
  title: str
  content: str
  images: list[SectionImage] = []


class EpochEvent(BaseModel):
  year: str
  title: str
  people: str
  description: str = ""
  image: str | None = None
  people_image: str | None = None
  images: list[str] = []
  sections: list[EventSection] = []


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
