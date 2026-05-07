from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.schemas_tenant import CreateTenant, UpdateTenant
from app.models.model_tenant import Tenant


class RepositoryTenant:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_tenant(self, data: CreateTenant) -> Tenant:
        tenant = Tenant(
            **data.model_dump()
        )
        self.session.add(tenant)
        await self.session.flush()
        await self.session.refresh(tenant)
        return tenant
    
    async def get_tenant(self, tenant_id: int) -> Tenant:
        tenant = await self.session.get(Tenant, tenant_id)
        return tenant
    
    async def get_tenants(self, limit: int, offset: int) -> list[Tenant]:
        tenants = await self.session.execute(
            select(Tenant)
            .limit(limit).offset(offset)
        )
        return tenants.scalars().all()
    
    async def update_tenant(self, tenant: Tenant, data: UpdateTenant) -> Tenant:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(tenant, field, value)
        self.session.add(tenant)
        await self.session.flush()
        await self.session.refresh(tenant)
        return tenant
    
    async def delete_tenant(self, tenant: Tenant):
        self.session.delete(tenant)