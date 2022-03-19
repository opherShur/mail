from uuid import UUID
from typing import Union

from pydantic import BaseModel, Field

from address import Address


class Letter(BaseModel):
    id: Union[UUID, int, str]
    sender_address: Address
    sender_name: str
    receiver_address: Address
    receiver_name: str
    content: str = Field(title="Content of letter", description="Cannot be longer than 1000 characters",
                         max_length=1000)
