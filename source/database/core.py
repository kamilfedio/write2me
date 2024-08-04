from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from source.models.base import Base
from source.config.config import Config

Config = Config()

engine = create_async_engine(Config.DB_ADDRESS, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def create_all_tabels():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
