from pydantic import BaseModel

from api.schemas.rent import Rent
from api.schemas.user import User


class Review(BaseModel):
    int: id
    sender: User
    sender_id: int
    rent: Rent
    rent_id: int
    rating: int
    comment: str

    class Config:
        orm_mode: True
    