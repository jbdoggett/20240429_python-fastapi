from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Generator

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency injected db sesssion
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notify", response_model=schemas.Notification)
def notify(notification: schemas.NotificationCreate,
           db: Session=Depends(get_db)) -> models.Notification:
    print(notification)
    print('hoo')
    return crud.create_notification(db, notification)
