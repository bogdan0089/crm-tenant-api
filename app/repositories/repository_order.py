from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas_order import CreateOrder, ResponseOrder, UpdateOrder
from app.models.model_order import Order
from sqlalchemy import select
from app.core.enums import OrderStatus


class RepositoryOrder:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order(self, data: CreateOrder) -> Order:
        order = Order(
            **data.model_dump()
        )
        self.session.add(order)
        await self.session.flush()
        await self.session.refresh(order)
        return order

    async def get_order(self, order_id: int) -> Order:
        order = await self.session.get(Order, order_id)
        return order
    
    async def get_orders(self, limit: int, offset: int) -> list[Order]:
        orders = await self.session.execute(
            select(Order)
            .limit(limit).offset(offset)
        )
        return orders.scalars().all()
    
    async def update_order(self, order: Order, data: UpdateOrder) -> Order:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(order, field, value)
        self.session.add(order)
        await self.session.flush()
        await self.session.refresh(order)
        return order
    
    async def update_order_status(self, order: Order, status: OrderStatus) -> Order:
        order.status = status
        self.session.add(order)
        await self.session.flush()
        await self.session.refresh(order)
        return order
    
    async def delete_order(self, order: Order):
        await self.session.delete(order)
        


