from sqlalchemy import Boolean, DateTime, Text, Integer, ForeignKey, Float
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from source.models.base import Base

class Rating(Base):
    __tablename__ = 'ratings'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('forms.id'), nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    form: Mapped['Form'] = relationship('Form', back_populates='ratings', lazy='selectin')