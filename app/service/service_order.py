from app.database.unit_of_work import UnitOfWork
from app.core.enums import OrderStatus
from app.schemas.schemas_order import CreateOrder, UpdateOrder
from app.models.model_order import Order
from app.core.exceptions import OrderNotFound


class ServiceOrder:

    @staticmethod
    async def create_order(data: CreateOrder) -> Order:
        async with UnitOfWork() as uow:
            order = await uow.order.create_order(data)
            return order
        
    @staticmethod
    async def get_order(order_id: int) -> Order:
        async with UnitOfWork() as uow:
            order = await uow.order.get_order(order_id)
            if not order:
                raise OrderNotFound(order_id)
            return order
        
    @staticmethod
    async def get_orders(limit: int, offset: int) -> list[Order]:
        async with UnitOfWork() as uow:
            return await uow.order.get_orders(limit, offset)
        
    @staticmethod
    async def update_order(order_id: int, data: UpdateOrder) -> Order:
        async with UnitOfWork() as uow:
            order = await uow.order.get_order(order_id)
            if not order:
                raise OrderNotFound(order_id)
            updated = await uow.order.update_order(order, data)
            return updated
        
    @staticmethod
    async def update_order_status(order_id: int, status: OrderStatus):
        async with UnitOfWork() as uow:
            order = await uow.order.get_order(order_id)
            if not order:
                raise OrderNotFound(order_id)
            updated = await uow.order.update_order_status(order, status)
            return updated

    @staticmethod
    async def delete_order(order_id: int):
        async with UnitOfWork() as uow:
            order = await uow.order.get_order(order_id)
            if not order:
                raise OrderNotFound(order_id)
            await uow.order.delete_order(order)





