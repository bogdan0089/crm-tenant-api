from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session_maker
from sqlalchemy.orm import DeclarativeBase
from core.config import settings


async_engine = create_async_engine(settings.DATABASE_URL)

session_maker = async_session_maker(bind=async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with session_maker() as session:
        yield session




