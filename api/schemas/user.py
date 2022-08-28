from typing import List

from pydantic import BaseModel

from api.schemas.building import Building
from api.schemas.list_response import ListResponse


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


class ListUserResponse(ListResponse):
    items: List[User] = []
