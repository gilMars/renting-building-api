import datetime

from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.config import Base


class Rent(Base):
    __tablename__ = 'rents'

    id = Column(Integer, primary_key=True, index=True)
    start = Column(DateTime, default=datetime.datetime.utcnow)
    end = Column(DateTime)

    # building_id = Column(Integer, ForeignKey('buildings.id'))
    # lodger_id = Column(Integer, ForeignKey('users.id'))
    # payment_id = Column(Integer, ForeignKey('payments.id'))
    # review_id = Column(Integer, ForeignKey('reviews.id'))

    # lodger = relationship('User')
    # building = relationship('Building')
    # payment = relationship('Payment')
    # review = relationship('Review', back_populates='rent')
