from fastapi import FastAPI, Status
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(title="Notification Service")

class NotificationSchema(BaseModel):
    recipient: str
    message: str

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "notification"}

@app.post("/notifications", status_code=Status.HTTP_201_CREATED)
async def create_notification(payload: NotificationSchema):
    return {
        "id": uuid4().hex,
        "recipient": payload.recipient,
        "message": payload.message,
        "status": "accepted"
    }