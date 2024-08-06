from sqlalchemy import DateTime, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime
from source.models.base import Base

class Form(Base):
    __tablename__ = 'forms'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    name: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped['User'] = relationship('User', back_populates='forms')
    contact_requests: Mapped[list['ContactRequest']] = relationship('ContactRequest', back_populates='form',
                                                                    lazy='selectin')
    reviews: Mapped[list['Review']] = relationship('Review', back_populates='form',
                                                   lazy='selectin')
    ratings: Mapped[list['Rating']] = relationship('Rating', back_populates='form',
                                                   lazy='selectin')
