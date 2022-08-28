from fastapi import FastAPI

from api.database import config
from api.database.config import engine
from api.routes import buildings, users

app = FastAPI()

config.Base.metadata.create_all(bind=engine)

app.include_router(buildings.router)
app.include_router(users.router)



