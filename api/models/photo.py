from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from api.database.config import Base


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    description = Column(String)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    building = relationship('Building', back_populates='photos')
