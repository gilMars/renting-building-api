from sqlalchemy.orm import Session

import models
from models.user import User
from schemas.user import UserBase


class UserRepository:

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def list_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def create_user(db: Session, user: UserBase):
        db_user = models.User(email=user.email, name=user.name, document=user.document,
                              address=user.address, cellphone=user.cellphone)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
