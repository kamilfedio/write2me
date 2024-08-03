from sqlalchemy import Boolean, DateTime, ForeignKey, Column, BigInteger
from datetime import datetime
from source.models.base import Base

class AccessToken(Base):
    __tablename__ = 'access_tokens'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    expired = Column(Boolean)
    date = Column(DateTime, default=datetime.now)
    