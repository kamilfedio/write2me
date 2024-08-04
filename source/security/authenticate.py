from datetime import datetime, timedelta, timezone
import secrets
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.users import User
from source.security.password import Password


class SecurityUtils:

    @staticmethod
    async def authenticate(email: str, password: str, session: AsyncSession) -> User | None:
        """
        checking if credentials are correct with database
        Args:
            email (str): user email
            password (str): user password
            session (AsyncSession): database session

        Returns:
            User | None: user or nothing
        """
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        user: User | None = result.scalar_one_or_none()

        if user is None:
            return None
        
        if not Password.verify_password(password, user.hashed_password):
            return None
        
        return user

    @staticmethod
    async def create_access_token(user: User, session: AsyncSession) -> AccessToken:
        """
        creating access token to database
        Args:
            user (User): user object
            session (AsyncSession): database session

        Returns:
            _type_: access token
        """

        access_token = AccessToken(user=user)
        session.add(access_token)
        await session.commit()
        return access_token
    
    @staticmethod
    def generate_token() -> str:
        """
        generating token
        Returns:
            str: token
        """
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def get_expiration_date(duration_seconds: int = 86400) -> datetime:
        """
        calculating expiration date
        Args:
            duration_seconds (int, optional): duration to expiration. Defaults to 86400.

        Returns:
            datetime: expiration date
        """
        return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)
    

from source.models.access_tokens import AccessToken
