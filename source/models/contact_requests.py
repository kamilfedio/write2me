from sqlalchemy import Boolean, DateTime, Text, Integer, ForeignKey
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from source.models.base import Base

class ContactRequest(Base):
    __tablename__ = 'contact_requests'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('forms.id'), nullable=False)
    name: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    read: Mapped[bool] = mapped_column(Boolean, default=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    form: Mapped['Form'] = relationship('Form', back_populates='contact_requests',
                                        lazy='selectin')
