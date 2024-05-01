from sqlalchemy.orm import Session

import models
import schemas

def create_notification(db: Session,
                        notification: schemas.NotificationCreate
                        ) -> models.Notification:
    db_notification = models.Notification(
        message=notification.message, email=notification.email)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
