from sqlalchemy import Boolean, DateTime, Text, Integer, ForeignKey, Float
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from source.models.base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('forms.id'), nullable=False)
    name: Mapped[str] = mapped_column(Text)
    positive: Mapped[bool] = mapped_column(Boolean)
    rating: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    form: Mapped['Form'] = relationship('Form', back_populates='reviews', lazy='selectin')