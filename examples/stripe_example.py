from billing_system import BillingSystem, Item
from billing_system.payment.stripe_gateway import StripeGateway

def main():
    # Initialize with Stripe
    stripe_gateway = StripeGateway("your_stripe_api_key")
    billing_system = BillingSystem(payment_gateway=stripe_gateway)
    
    # Register vendors
    vendor1 = billing_system.register_vendor("Electronics Store")
    vendor2 = billing_system.register_vendor("Book Store")
    
    # Create and process order
    order = billing_system.create_order()
    
    billing_system.add_item_to_order(order, 
        Item(item_id="laptop001", name="Laptop", price=1200.00, vendor_id=vendor1)
    )
    billing_system.add_item_to_order(order,
        Item(item_id="book001", name="Python Book", price=50.00, vendor_id=vendor2)
    )
    
    # Process payment
    result = billing_system.process_order_payment(
        order,
        payment_details={
            "payment_method_id": "pm_card_visa",
        }
    )
    
    print(f"Payment Result: {result}")

if __name__ == "__main__":
    main() 