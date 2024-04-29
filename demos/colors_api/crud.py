from sqlalchemy.orm import Session

import models_w_db
import schemas

def get_colors(db: Session) -> list[models_w_db.Color]:
    return db.query(models_w_db.Color).all()

def create_color(db: Session, color: schemas.ColorCreate) -> models_w_db.Color:
    db_color = models_w_db.Color(
        name=color.name, hex_code=color.hex_code)
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color
