from sqlalchemy import Boolean, DateTime, Text, Column, BigInteger, ForeignKey, Float
from datetime import datetime

from source.models.base import Base

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(BigInteger, primary_key=True)
    forms_id = Column(BigInteger, ForeignKey('forms.id'), nullable=False)
    rating = Column(Float)
    date = Column(DateTime, default=datetime.now)
