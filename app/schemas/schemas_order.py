from pydantic import BaseModel, ConfigDict
from app.core.enums import OrderStatus
from datetime import datetime

class CreateOrder(BaseModel):
    title: str
    amount: float
    status: OrderStatus = OrderStatus.NEW
    tenant_id: int

class ResponseOrder(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    amount: float
    status: OrderStatus
    tenant_id: int
    created_at: datetime

class UpdateOrder(BaseModel):
    title: str | None = None
    amount: float | None = None
    status: OrderStatus | None = None

class UpdateOrderStatus(BaseModel):
    status: OrderStatus

