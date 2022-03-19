from uuid import uuid4, UUID

from pydantic import BaseModel, Field

from address import Address


class Letter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    sender_address: Address
    sender_name: str
    receiver_address: Address
    receiver_name: str
    content: str = Field(title="Content of letter", description="Cannot be longer than 1000 characters",
                         max_length=1000)
