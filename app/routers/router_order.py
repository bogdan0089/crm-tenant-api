from fastapi import APIRouter
from app.schemas.schemas_order import CreateOrder, ResponseOrder, UpdateOrder
from app.core.enums import OrderStatus
from app.service.service_order import ServiceOrder


router_order = APIRouter(prefix="/orders", tags=["Orders"])


@router_order.post("/", response_model=ResponseOrder)
async def create_order(data: CreateOrder) -> ResponseOrder:
    return await ServiceOrder.create_order(data)

@router_order.get("/{order_id}", response_model=ResponseOrder)
async def get_order(order_id: int) -> ResponseOrder:
    return await ServiceOrder.get_order(order_id)

@router_order.get("/", response_model=list[ResponseOrder])
async def get_orders(limit: int = 10, offset: int = 0) -> list[ResponseOrder]:
    return await ServiceOrder.get_orders(limit, offset)

@router_order.patch("/{order_id}", response_model=ResponseOrder)
async def update_order(order_id: int, data: UpdateOrder) -> ResponseOrder:
    return await ServiceOrder.update_order(order_id, data)

@router_order.patch("/{order_id}/status", response_model=ResponseOrder)
async def update_order_status(order_id: int, status: OrderStatus) -> ResponseOrder:
    return await ServiceOrder.update_order_status(order_id, status)

@router_order.delete("/{order_id}", status_code=204)
async def delete_order(order_id: int):
    return await ServiceOrder.delete_order(order_id)
