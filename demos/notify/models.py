from sqlalchemy import Column, String, Integer

from database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    message = Column(String)
    email = Column(String)
