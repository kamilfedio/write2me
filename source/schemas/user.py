from pydantic import EmailStr

from source.schemas.access_token import AccessTokenRead
from source.schemas.base import Base
from source.schemas.form import FormReadShortcut

class UserBase(Base):
    nick: str
    email: EmailStr
    name_surname: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None

class UserReadBase(UserBase):
    id: int

class UserRead(UserBase):
    access_tokens: list[AccessTokenRead]
    forms: list[FormReadShortcut]
