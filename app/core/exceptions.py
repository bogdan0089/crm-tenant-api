from fastapi import HTTPException, status


class BaseAppExeptions(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class OrderNotFound(BaseAppExeptions):
    def __init__(self, order_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found."
        )

class OrdersNotFound(BaseAppExeptions):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Orders not found."
        )

class TenantNotFound(BaseAppExeptions):
    def __init__(self, tenant_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tenant {tenant_id} not found."
        )

class TenantsNotFound(BaseAppExeptions):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tenants not found."
        )


