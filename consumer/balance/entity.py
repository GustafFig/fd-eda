from uuid import uuid4, UUID
from pydantic import BaseModel, field_validator, Field


class BalanceBase(BaseModel):
    # TODO: IS IT REQUIRED?
    value: float

    @field_validator('value')
    def value_should_be_equal_or_bigger_than_0(cls, value):
        if value < 0:
            raise ValueError("Value should be bigger or equal 0")
        return value


class BalanceCreate(BaseModel):
    pass


class Balance(BalanceCreate):
    id: UUID = Field(default_factory=lambda: uuid4().hex)

    class Config:
        orm_mode = True
