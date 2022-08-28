from pydantic import BaseModel


class ListResponse(BaseModel):
    total: int
    count: int
