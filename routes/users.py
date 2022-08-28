import http
from typing import List

from fastapi import APIRouter, Depends
from requests import Session

import schemas
from database.config import get_db
from repositories.repository_facade import RepositoryFacade
from schemas.user import UserBase

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/', response_model=List[schemas.user.User])
async def users(db: Session = Depends(get_db)):
    return RepositoryFacade.list_users(db)


@router.get('/{user_id}', response_model=schemas.user.User)
async def user(user_id: int, db: Session = Depends(get_db)):
    return RepositoryFacade.get_user(db, user_id)


@router.post('/', response_model=schemas.user.User, status_code=http.HTTPStatus.CREATED)
async def create_user(user_to_insert: UserBase, db: Session = Depends(get_db)):
    return RepositoryFacade.create_user(db, user_to_insert)