from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from app.core.enums import OrderStatus
from app.database.session import Base
from datetime import datetime
from sqlalchemy import Enum as SAEnum



class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"))
    title: Mapped[str]
    amount: Mapped[float]
    status: Mapped[OrderStatus] = mapped_column(
        SAEnum(OrderStatus, values_callable=lambda x: [e.value for e in x]),
        default=OrderStatus.NEW
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    tenant: Mapped["Tenant"] = relationship(back_populates="orders")
