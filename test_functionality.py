from src.billing_system import BillingSystem, Item
from src.billing_system.payment.stripe_gateway import StripeGateway
from src.billing_system.shipping.calculator import ShippingCalculator
from src.billing_system.shipping.address import ShippingAddress
from src.billing_system.storage.database import DatabaseManager

def test_full_order_flow():
    # Initialize components
    shipping_rates = {
        "US": {"base_rate": 5.00, "per_item": 2.00},
        "CA": {"base_rate": 7.00, "per_item": 2.50}
    }
    
    shipping_calc = ShippingCalculator(rates=shipping_rates)
    stripe_gateway = StripeGateway("sk_test_your_key")
    db_manager = DatabaseManager("sqlite:///test.db")
    
    # Initialize billing system
    billing_system = BillingSystem(
        payment_gateway=stripe_gateway,
        shipping_calculator=shipping_calc
    )
    
    try:
        # 1. Register vendors
        electronics_vendor = billing_system.register_vendor("Electronics Store")
        books_vendor = billing_system.register_vendor("Book Store")
        
        print(f"Registered vendors successfully")
        
        # 2. Create order
        order = billing_system.create_order()
        print(f"Created order: {order.order_id}")
        
        # 3. Add items
        items = [
            Item(name="Laptop", price=999.99, vendor_id=electronics_vendor, quantity=1),
            Item(name="Python Book", price=49.99, vendor_id=books_vendor, quantity=2)
        ]
        
        for item in items:
            billing_system.add_item_to_order(order, item)
            print(f"Added item: {item.name} (${item.price} x {item.quantity})")
        
        # 4. Set shipping address
        shipping_address = ShippingAddress(
            street="123 Test St",
            city="Test City",
            state="CA",
            country="US",
            postal_code="12345"
        )
        
        # 5. Calculate final price
        final_price = billing_system.calculate_final_price(order, shipping_address)
        print(f"\nOrder Summary:")
        print(f"Subtotal: ${order.total_amount:.2f}")
        print(f"Final Price (with shipping): ${final_price:.2f}")
        
        # 6. Process payment
        payment_result = billing_system.process_order_payment(
            order,
            payment_details={"payment_method_id": "pm_card_visa"}
        )
        
        print(f"\nPayment Result: {payment_result}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_full_order_flow() 