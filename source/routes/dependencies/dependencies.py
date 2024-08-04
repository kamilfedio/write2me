from datetime import datetime, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from source.config.routes import RoutesConfig
from source.database.core import get_async_session
from source.models.users import User

class Dependencies:
    @staticmethod
    async def get_current_user(
        token: str = Depends(OAuth2PasswordBearer(tokenUrl=RoutesConfig.token)),
        session: AsyncSession = Depends(get_async_session)
    ) -> User:
        """
        searching in the database for a user with a given token
        Args:
            token (str, optional): input token
            session (AsyncSession, optional): database session
        Returns:
            User: user data
        """
        query = select(AccessToken).where(
            AccessToken.token == token,
            AccessToken.expiration_date >= datetime.now(tz=timezone.utc),
        )
        result = await session.execute(query)
        access_token: AccessToken | None = result.scalar_one_or_none()

        if access_token is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        return access_token.user

from source.models.access_tokens import AccessToken
