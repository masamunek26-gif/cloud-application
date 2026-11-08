import logging
import httpx
from app.config import settings

logger = logging.getLogger(__name__)

class NotificationClient:
    def __init__(self):
        self.base_url = settings.notification_service_url
        self.timeout = settings.notification_timeout_seconds
        self.max_attempts = settings.notification_max_attempts

    def send_notification(self, recipient: str, subject: str, body: str) -> bool:
        url = f"{self.base_url}/send"
        payload = {
            "recipient": recipient,
            "subject": subject,
            "body": body
        }

        for attempt in range(1, self.max_attempts + 1):
            try:
                with httpx.Client(timeout=self.timeout) as client:
                    response = client.post(url, json=payload)
                    if response.status_code == 200:
                        logger.info(f"Notification sent successfully to {recipient}")
                        return True
                    elif response.status_code in (502, 503, 504):
                        logger.warning(f"Attempt {attempt}/{self.max_attempts}: Server returned {response.status_code}, retrying...")
                    else:
                        logger.error(f"Failed to send notification: {response.status_code} - {response.text}")
                        return False
            except (httpx.TimeoutException, httpx.ConnectError) as e:
                logger.warning(f"Attempt {attempt}/{self.max_attempts}: Connection error/timeout ({e}), retrying...")

        logger.error("All attempts to send notification failed.")
        return False

notification_client = NotificationClient()