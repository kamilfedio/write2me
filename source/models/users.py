from sqlalchemy import DateTime, Text, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime
from source.models.base import Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(Text, unique=True)
    name_surname: Mapped[str] = mapped_column(Text)
    nick: Mapped[str] = mapped_column(Text)
    hashed_password: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    forms: Mapped[list['Form']] = relationship('Form', back_populates='user', lazy='selectin')