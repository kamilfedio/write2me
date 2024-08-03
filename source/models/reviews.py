from sqlalchemy import DateTime, Text, Column, BigInteger, ForeignKey, Float
from datetime import datetime

from source.models.base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(BigInteger, primary_key=True)
    forms_id = Column(BigInteger, ForeignKey('forms.id'), nullable=False)
    name = Column(Text)
    rating = Column(Float)
    date = Column(DateTime, default=datetime.now)
