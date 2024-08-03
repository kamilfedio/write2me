from datetime import datetime
from pydantic import Field
from source.schemas.base import Base
from enum import Enum

from source.schemas.contact_request import ContactRequestRead
from source.schemas.rating import RatingRead
from source.schemas.review import ReviewRead

class FormType(str, Enum):
    rating: str = 'rating'
    review: str = 'review'
    contact_request: str = 'contact_request'

class FormBase(Base):
    type: FormType
    description: str
    name: str

class FormCreate(FormBase):
    date = Field(default=datetime.now)

class FormUpdate(FormBase):
    description: str | None = None
    name: str | None = None

class FormReadShortcut(FormBase):
    id: int

class FormRead(FormReadShortcut):
    contact_requests: list[ContactRequestRead]
    reviews: list[ReviewRead]
    ratings: list[RatingRead]
