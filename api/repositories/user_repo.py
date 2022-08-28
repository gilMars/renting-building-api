from sqlalchemy.orm import Session

from api.models.user import User
from api.schemas.user import UserBase, ListUserResponse


class UserRepository:

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def list_users(db: Session, offset: int, limit: int):
        initial_query = db.query(User)
        final_query = initial_query.offset(offset).limit(limit)
        total = initial_query.count()
        count = final_query.count()
        return ListUserResponse(items=final_query.all(), total=total, count=count)

    @staticmethod
    def create_user(db: Session, user: UserBase):
        db_user = User(email=user.email, name=user.name, document=user.document,
                       address=user.address, cellphone=user.cellphone)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
