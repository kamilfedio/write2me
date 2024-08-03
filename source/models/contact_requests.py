from sqlalchemy import Boolean, DateTime, Text, Column, BigInteger, ForeignKey
from datetime import datetime

from source.models.base import Base

class ContactRequest(Base):
    __tablename__ = 'contact_requests'
    id = Column(BigInteger)
    forms_id = Column(BigInteger, ForeignKey('forms.id'), nullable=False)
    name = Column(Text)
    email = Column(Text)
    content = Column(Text)
    read = Column(Boolean)
    date = Column(DateTime, default=datetime.now)
