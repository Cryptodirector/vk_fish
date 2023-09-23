from database import async_session_maker
from sqlalchemy import insert
from models import VkAccount


async def save(**data):
    async with async_session_maker() as session:
        stmt = insert(VkAccount).values(**data)
        await session.execute(stmt)
        await session.commit()