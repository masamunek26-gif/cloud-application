from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.security.authorization import require_permission
from app.integrations.notification_client import send_notification, NotificationServiceError

router = APIRouter(prefix="/integration", tags=["Integration"])

class NotificationRequest(BaseModel):
    recipient: str
    message: str

@router.post("/notifications", status_code=status.HTTP_201_CREATED)
async def trigger_notification(
    data: NotificationRequest,
    user=Depends(require_permission("services.write"))
):
    try:
        result = await send_notification(data.recipient, data.message)
        return result
    except NotificationServiceError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc)
        )