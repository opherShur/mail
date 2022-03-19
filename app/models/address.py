from typing import Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    number: int
    floor: Optional[int] = Field(default=0)
    apartment: int
    extra: Optional[str] = Field(default="")
