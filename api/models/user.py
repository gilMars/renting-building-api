from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.database.config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    document = Column(String, unique=True)
    address = Column(String)
    email = Column(String)
    cellphone = Column(String)
    
    buildings = relationship('Building', back_populates='owner')
