from fastapi import APIRouter
from app.schemas.schemas_tenant import CreateTenant, ResponseTenant, UpdateTenant
from app.service.service_tenant import ServiceTenant


router_tenant = APIRouter(prefix="/tenants", tags=["Tenants"])


@router_tenant.post("/", response_model=ResponseTenant)
async def create_tenant(data: CreateTenant) -> ResponseTenant:
    return await ServiceTenant.create_tenant(data)

@router_tenant.get("/{tenant_id}", response_model=ResponseTenant)
async def get_tenant(tenant_id: int) -> ResponseTenant:
    return await ServiceTenant.get_tenant(tenant_id)

@router_tenant.get("/", response_model=list[ResponseTenant])
async def get_tenants(limit: int = 10, offset: int = 0) -> list[ResponseTenant]:
    return await ServiceTenant.get_tenants(limit, offset)

@router_tenant.patch("/{tenant_id}", response_model=ResponseTenant)
async def update_tenant(tenant_id: int, data: UpdateTenant) -> ResponseTenant:
    return await ServiceTenant.update_tenant(tenant_id, data)

@router_tenant.delete("/{tenant_id}", status_code=204)
async def delete_tenant(tenant_id: int):
    return await ServiceTenant.delete_tenant(tenant_id)
