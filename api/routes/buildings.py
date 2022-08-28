import http
from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from api import schemas
from api.database.config import get_db
from api.repositories.repository_facade import RepositoryFacade

router = APIRouter()


@router.post('/users/{user_id}/buildings', response_model=schemas.building.Building, status_code=http.HTTPStatus.CREATED)
async def create_building(user_id: int, building_to_insert: schemas.building.BuildingBase,
                          db: Session = Depends(get_db)):
    return RepositoryFacade.create_building(db, building_to_insert, user_id)


@router.get('/buildings')
async def list_buildings(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return RepositoryFacade.list_buildings(db, offset, limit)
