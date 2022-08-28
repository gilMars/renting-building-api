from typing import List

from pydantic import BaseModel

from api.schemas.list_response import ListResponse
from api.schemas.photo import Photo


class BuildingBase(BaseModel):
    name: str
    address: str
    description: str
    photos: List[Photo] = []


class Building(BuildingBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ListBuildingResponse(ListResponse):
    items: List[Building] = []