from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Generator

import crud
import models_w_db
import schemas
from database import SessionLocal, engine

models_w_db.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency injected db sesssion
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/colors", response_model=list[schemas.Color])
async def all_colors(db: Session = Depends(get_db)) -> list[models_w_db.Color]:
    return crud.get_colors(db)


@app.post("/colors", response_model=schemas.Color)
async def create_color(color: schemas.ColorCreate,
                       db: Session=Depends(get_db)) -> models_w_db.Color:
    return crud.create_color(db, color)
