from app.database.unit_of_work import UnitOfWork
from app.schemas.schemas_tenant import CreateTenant, UpdateTenant
from app.models.model_tenant import Tenant
from app.core.exceptions import TenantNotFound, TenantsNotFound


class ServiceTenant:

    @staticmethod
    async def create_tenant(data: CreateTenant) -> Tenant:
        async with UnitOfWork() as uow:
            tenant = await uow.tenant.create_tenant(data)
            return tenant
        
    @staticmethod
    async def get_tenant(tenant_id: int) -> Tenant:
        async with UnitOfWork() as uow:
            tenant = await uow.tenant.get_tenant(tenant_id)
            if not tenant:
                raise TenantNotFound(tenant_id)
            return tenant
        
    @staticmethod
    async def get_tenants(limit: int, offset: int) -> list[Tenant]:
        async with UnitOfWork() as uow:
            tenants = await uow.tenant.get_tenants(limit, offset)
            if not tenants:
                raise TenantsNotFound()
            return tenants
        
    @staticmethod
    async def update_tenant(tenant_id: int, data: UpdateTenant) -> Tenant:
        async with UnitOfWork() as uow:
            tenant = await uow.tenant.get_tenant(tenant_id)
            if not tenant:
                raise TenantNotFound(tenant_id)
            updated = await uow.tenant.update_tenant(tenant, data)
            return updated
        
    @staticmethod
    async def delete_tenant(tenant_id: int):
        async with UnitOfWork() as uow:
            tenant = await uow.tenant.get_tenant(tenant_id)
            if not tenant:
                raise TenantNotFound(tenant_id)
            await uow.tenant.delete_tenant(tenant)