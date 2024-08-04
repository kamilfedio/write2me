from pydantic import EmailStr

from source.schemas.base import Base
from source.schemas.form import FormReadShortcut

class UserBase(Base):
    nick: str
    email: EmailStr
    name_surname: str

class UserCreate(UserBase):
    password: str

class UserUpdate(Base):
    email: EmailStr | None = None
    nick: str | None = None

class UserUpdatePassword(Base):
    old_password: str
    password: str

class UserReadBase(UserBase):
    id: int

class UserRead(UserBase):
    forms: list[FormReadShortcut]
