from uuid import uuid4, UUID

from typing import Optional
from pydantic import BaseModel, Field

from app.models.address import Address


class Letter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    sender_address: Optional[Address] = Field(default=None, title="Address of sender")
    sender_name: Optional[str] = Field(default="", title="Name of sender")
    receiver_address: Address = Field(title="Address of receiver")
    receiver_name: Optional[str] = Field(default="", title="Name of receiver")
    content: str = Field(title="Content of letter", description="Cannot be longer than 1000 characters",
                         max_length=1000)
