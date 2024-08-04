from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from source.database.core import get_async_session
from source.models.access_tokens import AccessToken
from source.routes.dependencies.dependencies import Dependencies
from source.security.authenticate import SecurityUtils


router = APIRouter()

@router.post('/')
async def create_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    session: AsyncSession = Depends(get_async_session)
):
    email = form_data.username
    password = form_data.password
    user = await SecurityUtils.authenticate(email, password, session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    token = await SecurityUtils.create_access_token(user, session)

    return {'access_token': token.token, 'token_type': 'bearer'}
