from abc import ABC, abstractmethod
from ..models import Order

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> bool:
        pass

class EmailNotification(NotificationService):
    def __init__(self, smtp_settings: dict):
        self.smtp_settings = smtp_settings
        
    def send_notification(self, recipient: str, message: str) -> bool:
        # Implement email sending logic
        pass 