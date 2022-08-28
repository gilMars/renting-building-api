from datetime import datetime

from pydantic import BaseModel

from schemas.building import Building
from schemas.payment import Payment
from schemas.review import Review
from schemas.user import User


class Rent(BaseModel):
    id: int
    building: Building
    building_id: int
    lodger: User
    lodger_id: int
    start: datetime
    end: datetime
    payment: Payment
    payment_id = int
    review: Review
    review_id: int

    class Config:
        orm_mode = True
