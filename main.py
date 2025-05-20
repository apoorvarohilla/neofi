from fastapi import FastAPI
from . import models, database, auth, events

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(events.router)
