from sqlalchemy.orm import Session

import models
from schemas.building import BuildingBase


class BuildingRepository:

    @staticmethod
    def create_building(db: Session, building: BuildingBase, user_id: int):
        db_building = models.Building(**building.dict(), owner_id=user_id)
        db.add(db_building)
        db.commit()
        db.refresh(db_building)
        return db_building

    @staticmethod
    def list_buildings(db: Session):
        return db.query(models.Building).all()
