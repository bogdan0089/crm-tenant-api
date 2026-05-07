from pydantic import BaseModel, EmailStr, ConfigDict


class CreateTenant(BaseModel):
    name: str
    email: EmailStr

class ResponseTenant(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr

class UpdateTenant(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
