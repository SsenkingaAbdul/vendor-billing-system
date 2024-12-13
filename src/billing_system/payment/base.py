from abc import ABC, abstractmethod
from typing import Dict, Any
from ..models import Order

class PaymentGateway(ABC):
    """Base class for payment gateway implementations."""
    
    @abstractmethod
    def process_payment(self, order: Order, payment_details: Dict[str, Any]) -> Dict[str, Any]:
        """Process a payment for an order."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        """Refund a payment."""
        pass 