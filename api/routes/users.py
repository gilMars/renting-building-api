import http
from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from api import schemas
from api.database.config import get_db
from api.repositories.repository_facade import RepositoryFacade
from api.schemas.user import UserBase

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
async def users(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return RepositoryFacade.list_users(db, offset, limit)


@router.get('/{user_id}', response_model=schemas.user.User)
async def user(user_id: int, db: Session = Depends(get_db)):
    return RepositoryFacade.get_user(db, user_id)


@router.post('/', response_model=schemas.user.User, status_code=http.HTTPStatus.CREATED)
async def create_user(user_to_insert: UserBase, db: Session = Depends(get_db)):
    return RepositoryFacade.create_user(db, user_to_insert)
