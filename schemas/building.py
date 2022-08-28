from typing import List

from pydantic import BaseModel

from schemas.photo import Photo


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
