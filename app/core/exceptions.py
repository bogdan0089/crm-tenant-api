from fastapi import HTTPException, status


class BaseAppExceptions(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class OrderNotFound(BaseAppExceptions):
    def __init__(self, order_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found."
        )

class TenantNotFound(BaseAppExceptions):
    def __init__(self, tenant_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tenant {tenant_id} not found."
        )

