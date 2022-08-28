import datetime

from sqlalchemy import Integer, Column, String, DateTime

from api.database.config import Base


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    payment_type = Column(String)
    receipt = Column(String)
    transaction = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    # sender_id = Column(Integer, ForeignKey('users.id'))
    # receiver_id = Column(Integer, ForeignKey('users.id'))

    # sender = relationship('User')
    # receiver = relationship('User')
