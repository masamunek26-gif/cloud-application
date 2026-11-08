from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Notification Service", version="1.0")

class NotificationMessage(BaseModel):
    recipient: EmailStr
    subject: str
    body: str

@app.post("/send")
def send_notification(notification: NotificationMessage):
    print(f"[NOTIFICATION SERVICE] Sending email to {notification.recipient}: '{notification.subject}'")
    return {
        "status": "success",
        "message": f"Notification successfully sent to {notification.recipient}"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}