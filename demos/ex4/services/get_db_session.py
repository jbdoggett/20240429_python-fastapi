from typing import Generator
from database import SessionLocal
from sqlalchemy.orm import Session

# Dependency injected db sesssion
def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
