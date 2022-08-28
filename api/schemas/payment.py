from datetime import datetime

from pydantic import BaseModel

from api.schemas.user import User


class Payment(BaseModel):
    id: int
    payment_type: str
    receipt: str
    transaction: str
    date: datetime
    sender: User
    receiver: User

    sender_id: int
    receiver_id: int

    class Config:
        orm_mode = True
