from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./tools_app.sqlite3"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# Foctory for creating new database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

