from sqlalchemy import Boolean, DateTime, ForeignKey, Text, Integer
from datetime import datetime
from source.models.base import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from source.security.authenticate import SecurityUtils

class AccessToken(Base):
    __tablename__ = 'access_tokens'

    token: Mapped[str] = mapped_column(Text, primary_key=True, default=SecurityUtils.generate_token)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, default=SecurityUtils.get_expiration_date)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped['User'] = relationship("User", lazy='joined')