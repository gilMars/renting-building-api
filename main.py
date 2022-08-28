from fastapi import FastAPI

from database import config
from database.config import engine
from routes import buildings, users

app = FastAPI()

config.Base.metadata.create_all(bind=engine)

app.include_router(buildings.router)
app.include_router(users.router)



