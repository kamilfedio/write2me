from sqlalchemy import DateTime, Text, Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from source.models.base import Base

class Form(Base):
    __tablename__ = 'forms'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    type = Column(Text)
    description = Column(Text)
    name = Column(Text)
    date = Column(DateTime, default=datetime.now)

    contact_requests = relationship('ContactRequest', backref='form')
    reviews = relationship('Reviews', backref='form')
    ratings = relationship('Ratings', backref='form')
