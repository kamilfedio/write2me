from datetime import datetime
from pydantic import Field
from source.schemas.base import Base

class RatingBase(Base):
    rating: float
    date: datetime

class RatingCreate(RatingBase):
    date: datetime = Field(default_factory=datetime.now)

class RatingRead(RatingBase):
    id: int
    forms_id: int
    