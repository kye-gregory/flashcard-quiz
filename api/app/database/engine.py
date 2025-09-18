import logging
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config.loader import settings
from .base import Base

engine = create_async_engine(settings.DB_URL)
async_session = async_sessionmaker(engine)


async def setup_database():
    logging.getLogger("aiosqlite").setLevel(logging.WARNING)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
