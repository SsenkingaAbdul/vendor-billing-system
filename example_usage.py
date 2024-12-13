from src.billing_system.core import BillingSystem, Item

def main():
    # Initialize the billing system
    billing_system = BillingSystem()
    
    # Register vendors
    electronics_vendor = billing_system.register_vendor("Electronics Store")
    clothing_vendor = billing_system.register_vendor("Fashion Outlet")
    
    # Create a customer order
    customer_order = billing_system.create_order()
    
    # Add items from different vendors
    billing_system.add_item_to_order(customer_order, 
        Item(item_id="laptop001", name="Gaming Laptop", price=1200.00, vendor_id=electronics_vendor)
    )
    billing_system.add_item_to_order(customer_order, 
        Item(item_id="shirt001", name="Casual Shirt", price=50.00, vendor_id=clothing_vendor)
    )
    
    # Process the order payment
    vendor_payments = billing_system.process_order_payment(customer_order)
    
    # Print order details
    print(f"Order ID: {customer_order.order_id}")
    print(f"Total Order Amount: ${customer_order.total_amount:.2f}")
    print("Vendor Payments:")
    for vendor_id, payment in vendor_payments.items():
        vendor_name = billing_system.vendors[vendor_id]
        print(f"- {vendor_name}: ${payment:.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")