from datetime import datetime, timedelta, timezone
import secrets
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.users import User
from source.security.password import Password


class SecurityUtils:

    @staticmethod
    async def authenticate(email: str, password: str, session: AsyncSession) -> User | None:
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        user: User | None = result.scalar_one_or_none()

        if user is None:
            return None
        
        if not Password.verify_password(password, user.hashed_password):
            return None
        
        return user

    @staticmethod
    async def create_access_token(user: User, session: AsyncSession):
        from source.models.access_tokens import AccessToken

        access_token = AccessToken(user=user)
        session.add(access_token)
        await session.commit()
        return access_token
    
    @staticmethod
    def generate_token() -> str:
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def get_expiration_date(duration_seconds: int = 86400) -> datetime:
        return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)
    