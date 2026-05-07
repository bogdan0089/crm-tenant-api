from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import session_maker
from app.repositories.repository_order import RepositoryOrder
from app.repositories.repository_tenant import RepositoryTenant

class UnitOfWork:
    def __init__(self) -> None:
        self.session: AsyncSession | None = None
        self.session_factory = session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.order = RepositoryOrder(self.session)
        self.tenant = RepositoryTenant(self.session)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
