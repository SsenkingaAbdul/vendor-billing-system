from abc import ABC, abstractmethod
from typing import Dict
from ..models import Order

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, order: Order, payment_details: Dict) -> Dict:
        """Process payment for an order and return transaction details"""
        pass

class DummyPaymentGateway(PaymentGateway):
    def process_payment(self, order: Order, payment_details: Dict) -> Dict:
        """Simulate payment processing"""
        return {
            "success": True,
            "transaction_id": "dummy_transaction",
            "amount": order.total_amount,
            "vendor_payments": order.vendor_payments
        } 