from typing import List

from pydantic import BaseModel

from schemas.building import Building


class UserBase(BaseModel):

    name: str
    document: str
    address: str
    email: str
    cellphone: str

    buildings: List[Building] = []


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
