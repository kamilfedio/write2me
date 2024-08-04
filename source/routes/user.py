from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from source.database.core import get_async_session
from source.models.users import User
from source.routes.dependencies.dependencies import Dependencies
from source.schemas.user import UserRead, UserUpdate, UserUpdatePassword
from source.security.password import Password

router = APIRouter()

@router.get('/me', response_model=UserRead)
async def get_user_me(user: User = Depends(Dependencies.get_current_user)) -> User:
    """
    returning current user
    Args:
        user (User, optional): getting current user.

    Returns:
        User: user data
    """
    return user

@router.patch('/me/update', response_model=UserRead)
async def user_me_update( user_update: UserUpdate,
                      user: User = Depends(Dependencies.get_current_user),
                      session: AsyncSession = Depends(get_async_session)) -> User:
    """
    updating user data
    Args:
        user_update (UserUpdate): updated user data
        user (User, optional): current user data
        session (AsyncSession, optional): database session

    Returns:
        User: user data
    """
    user_update_dict = user_update.model_dump(exclude_unset=True)
    for k,v in user_update_dict.items():
        setattr(user, k, v)

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


@router.patch('/me/change_password', response_model=UserRead)
async def user_me_change_password(user_update: UserUpdatePassword,
                               user: User = Depends(Dependencies.get_current_user),
                               session: AsyncSession = Depends(get_async_session)) -> User:
    """
    changing user password
    Args:
        user_update (UserUpdate): updated user data
        user (User, optional): current user data
        session (AsyncSession, optional): database session

    Returns:
        User: user data
    """
    if not Password.verify_password(hashed_password=user.hashed_password, plain_password = user_update.old_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    password = Password.get_password_hash(user_update.password)
    setattr(user, 'hashed_password', password)

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user