import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from api.database.config import get_db
from api.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


mocked_user_body = {
    'name': 'Dummy Name',
    'document': str(uuid.uuid4()),
    'address': 'Dummy Address',
    'email': 'a@a.com',
    'cellphone': '0800',
}


def create_user():
    return client.post('/users/', json=mocked_user_body)
