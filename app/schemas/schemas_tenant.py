from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class CreateTenant(BaseModel):
    name: str
    email: EmailStr

class ResponseTenant(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    created_at: datetime

class UpdateTenant(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
