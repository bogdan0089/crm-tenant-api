from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from app.database.session import Base
from datetime import datetime
from typing import List


class Tenant(Base):
    __tablename__ = "tenants"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    orders: Mapped[List["Order"]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    