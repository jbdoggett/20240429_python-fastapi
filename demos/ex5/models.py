# from sqlalchemy import String
from sqlalchemy import Column, Integer, String

from database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String)
