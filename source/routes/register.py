from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc

from source.database.core import get_async_session
from source.models.users import User
from source.schemas.user import UserCreate, UserRead
from source.security.password import Password

router = APIRouter()

@router.post('/', response_model=UserRead)
async def register(
    user_create: UserCreate, session: AsyncSession = Depends(get_async_session)
) -> User:
    """
    adding user to database
    Args:
        user_create (UserCreate): user creating data
        session (AsyncSession, optional): database session
    Returns:
        User: user data
    """
    hashed_password = Password.get_password_hash(user_create.password)

    user = User(
        **user_create.model_dump(exclude={'password'}),
        hashed_password=hashed_password
    )

    try:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exists'
        )
    
    return user