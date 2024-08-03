from sqlalchemy import DateTime, Text, Column, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime

from source.models.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    email = Column(Text)
    name_surname = Column(Text)
    nick = Column(Text)
    hashed_password = Column(Text)
    date = Column(DateTime, default=datetime.now)
    
    access_tokens = relationship('AccessToken', backref='user')
    forms = relationship('Form', backref='user')
