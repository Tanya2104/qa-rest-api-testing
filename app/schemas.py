from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

Name = Annotated[str, Field(min_length=1, max_length=150)]


class UserBase(BaseModel):
    name: Name
    email: EmailStr
    age: Annotated[int, Field(ge=18, le=100)]

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Name must not be blank")
        return value


class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8)]


class UserUpdate(UserCreate):
    pass


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    name: Name
    price: Annotated[float, Field(gt=0)]
    stock: Annotated[int, Field(ge=0)]

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Name must not be blank")
        return value


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: Annotated[int, Field(gt=0)]


class OrderResponse(OrderCreate):
    id: int
    total_price: float
    status: str
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class ErrorResponse(BaseModel):
    detail: str
