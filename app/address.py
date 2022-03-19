from pydantic import BaseModel


class Address(BaseModel):
    street: str
    number: int
    floor: int
    apartment: int
    extra: str
