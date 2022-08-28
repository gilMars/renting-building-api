from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from database.config import Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String)
    # rent_id = Column(Integer, ForeignKey('rents.id'))

    # rent = relationship('Review', back_populates='review')
    # photos = relationship('Photo', back_populates='building')
