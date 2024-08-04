from datetime import datetime
from pydantic import Field
from source.schemas.base import Base

class ReviewBase(Base):
    name: str
    rating: str
    date: datetime

class ReviewCreate(ReviewBase):
    date: datetime = Field(default_factory=datetime.now)

class ReviewRead(ReviewBase):
    id: int
    forms_id: int
    date: datetime