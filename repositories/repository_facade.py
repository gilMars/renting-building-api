from sqlalchemy.orm import Session

from repositories.building_repo import BuildingRepository
from repositories.user_repo import UserRepository
from schemas.building import BuildingBase
from schemas.user import UserBase


class RepositoryFacade:

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_user(db, user_id)

    @staticmethod
    def list_users(db: Session):
        return UserRepository.list_users(db)

    @staticmethod
    def create_user(db: Session, user: UserBase):
        return UserRepository.create_user(db, user)

    @staticmethod
    def create_building(db: Session, building: BuildingBase, user_id: int):
        return BuildingRepository.create_building(db, building, user_id)

    @staticmethod
    def list_buildings(db: Session):
        return BuildingRepository.list_buildings(db)
