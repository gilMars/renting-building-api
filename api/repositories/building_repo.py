from sqlalchemy.orm import Session

from api import models
from api.schemas.building import BuildingBase, ListBuildingResponse


class BuildingRepository:

    @staticmethod
    def create_building(db: Session, building: BuildingBase, user_id: int):
        db_building = models.Building(**building.dict(), owner_id=user_id)
        db.add(db_building)
        db.commit()
        db.refresh(db_building)
        return db_building

    @staticmethod
    def list_buildings(db: Session, offset: int, limit: int):
        initial_query = db.query(models.Building)
        total = initial_query.count()
        final_query = initial_query.offset(offset).limit(limit)
        count = final_query.count()
        return ListBuildingResponse(items=final_query.all(), total=total, count=count)
