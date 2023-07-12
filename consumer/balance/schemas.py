from uuid import uuid4, UUID
from pydantic import BaseModel, field_validator, Field


class AccountBase(BaseModel):
    id: str
    # TODO: IS IT REQUIRED?
    value: float

    @field_validator('value')
    def value_should_be_equal_or_bigger_than_0(cls, value):
        if value < 0:
            raise ValueError("Value should be bigger or equal 0")
        return value

    @field_validator('id')
    def id_should_be_an_uuid(cls, id):
        try:
            UUID(id)
        except ValueError as err:
            raise ValueError(f"Id should be an uuid not a {type(id)} - {err}")
        return str(id)


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):

    class Config:
        from_attributes = True
