from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import Sequence, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from source.database.core import get_async_session
from source.models.users import User
from source.models.forms import Form
from source.routes.dependencies.dependencies import Dependencies
from source.schemas.form import FormReadShortcut, FormRead, FormCreate

router = APIRouter()

@router.get('/', response_model=list[FormReadShortcut])
async def get_user_forms(
    user: User = Depends(Dependencies.get_current_user_public),
    session: AsyncSession = Depends(get_async_session),
    pagination: tuple[int, int] = Depends(Dependencies.pagination)
) -> Sequence[FormReadShortcut]:
    skip, limit = pagination
    select_query = select(Form).where(Form.id == user.id).offset(skip).limit(limit)
    res = await session.execute(select_query)
    
    return res.scalars().all()

@router.get('/{id}', response_model=FormRead)
async def get_user_form(
    id: str,
    session: AsyncSession = Depends(get_async_session),
    user: AsyncSession = Depends(Dependencies.get_current_user_public)
) -> FormRead:
    select_query = select(Form).where(Form.id == id)
    res = await session.execute(select_query)
    form: Form | None = res.scalar_one_or_none()
    if form is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return form

@router.post('/', response_model=FormReadShortcut)
async def create_form(
    form: FormCreate,
    user: User = Depends(Dependencies.get_current_user_private),
    session: AsyncSession = Depends(get_async_session)
) -> FormReadShortcut:
    new_form = Form(**form.model_dump(), user=user)
    session.add(new_form)
    await session.commit()
    await session.refresh(new_form)

    return new_form

@router.delete('/{id}')
async def delete_form(
    id: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(Dependencies.get_current_user_private)
):
    delete_query = delete(Form).where(Form.id == id)
    await session.execute(delete_query)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
