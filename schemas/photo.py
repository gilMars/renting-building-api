from pydantic import BaseModel


class Photo(BaseModel):
    id: int
    uri: str
    description: str
    building_id: int

    class Config:
        orm_mode = True
