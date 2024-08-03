from datetime import datetime
from pydantic import Field
from source.schemas.base import Base

class ContactRequestBase(Base):
    name: str
    email: str
    content: str

class ContactRequestCreate(ContactRequestBase):
    read: bool = Field(default=False)
    date: datetime = Field(default_factory=datetime.now)

class ContactRequestUpdate(Base):
    read: bool | None = None

class ContactRequestRead(ContactRequestBase):
    id: int
    forms_id: int
