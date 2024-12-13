from src.billing_system.core import BillingSystem
from src.billing_system.models import Item
from src.billing_system.shipping.address import ShippingAddress
from src.billing_system.payment.base import DummyPaymentGateway
from src.billing_system.shipping.calculator import ShippingCalculator

def main():
    # Initialize the billing system with required components
    billing = BillingSystem(
        payment_gateway=DummyPaymentGateway(),
        shipping_calculator=ShippingCalculator()
    )

    # Register a vendor
    vendor_id = billing.register_vendor("Example Store")
    print(f"Registered vendor: {vendor_id}")

    # Create an order
    order = billing.create_order()
    print(f"Created order: {order.order_id}")

    # Add items to the order
    items = [
        Item("Product 1", 29.99, vendor_id, quantity=2),
        Item("Product 2", 49.99, vendor_id, quantity=1),
    ]
    
    for item in items:
        billing.add_item_to_order(order, item)
        print(f"Added item: {item.name} (${item.price} x {item.quantity})")

    # Set shipping address
    address = ShippingAddress("123 Main St", "Example City", "EX", "12345")
    
    # Calculate final price including shipping
    final_price = billing.calculate_final_price(order, address)
    print(f"\nOrder Summary:")
    print(f"Subtotal: ${order.total_amount:.2f}")
    print(f"Final Price (with shipping): ${final_price:.2f}")
    
    # Process payment
    payment_details = {
        "card_number": "4111111111111111",
        "expiry": "12/25",
        "cvv": "123"
    }
    
    payment_result = billing.process_order_payment(order, payment_details)
    print(f"\nPayment processed: {payment_result}")

if __name__ == "__main__":
    main() 