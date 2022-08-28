from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from api.database.config import Base


class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    description = Column(String)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='buildings')
    photos = relationship('Photo', back_populates='building')
