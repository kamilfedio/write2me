from datetime import datetime
from pydantic import Field

from source.schemas.base import Base

class AccessToken(Base):
    id: int
    user_id: int
    expired: bool
    date: datetime = Field(default_factory=datetime.now)

class AccessTokenUpdate(Base):
    expired: bool | None = None

class AccessTokenRead(AccessToken):
    pass