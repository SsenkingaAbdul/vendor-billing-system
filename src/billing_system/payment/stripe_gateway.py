import stripe
from typing import Dict, Any
from .base import PaymentGateway
from ..models import Order

class StripeGateway(PaymentGateway):
    def __init__(self, api_key: str):
        stripe.api_key = api_key
        
    def process_payment(self, order: Order, payment_details: Dict[str, Any]) -> Dict[str, Any]:
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(order.total_amount * 100),  # Convert to cents
                currency="usd",
                payment_method=payment_details["payment_method_id"],
                confirm=True,
            )
            return {
                "success": True,
                "transaction_id": payment_intent.id,
                "status": payment_intent.status,
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
            }
    
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        try:
            refund = stripe.Refund.create(
                payment_intent=transaction_id,
                amount=int(amount * 100),
            )
            return {
                "success": True,
                "refund_id": refund.id,
                "status": refund.status,
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
            } 