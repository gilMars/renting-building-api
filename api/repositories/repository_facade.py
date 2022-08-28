from sqlalchemy.orm import Session

from api.repositories.building_repo import BuildingRepository
from api.repositories.user_repo import UserRepository
from api.schemas.building import BuildingBase
from api.schemas.user import UserBase


class RepositoryFacade:

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_user(db, user_id)

    @staticmethod
    def list_users(db: Session, offset: int, limit: int):
        return UserRepository.list_users(db, offset, limit)

    @staticmethod
    def create_user(db: Session, user: UserBase):
        return UserRepository.create_user(db, user)

    @staticmethod
    def create_building(db: Session, building: BuildingBase, user_id: int):
        return BuildingRepository.create_building(db, building, user_id)

    @staticmethod
    def list_buildings(db: Session, offset: int, limit: int):
        return BuildingRepository.list_buildings(db, offset, limit)
