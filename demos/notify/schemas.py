from pydantic import BaseModel

class BaseNotification(BaseModel):
    message: str
    email: str

class NotificationCreate(BaseNotification): ...

class Notification(BaseNotification):
    id: int

