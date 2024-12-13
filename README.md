# Vendor Billing Library

A flexible Python library for managing multi-vendor billing and order processing with support for multiple payment gateways.

## Installation
```bash
pip install vendor-billing-system
```

## Features
- Multiple payment gateway support (Stripe, PayPal)
- Vendor management
- Order processing
- Automatic payment distribution
- Comprehensive error handling

## Quick Start
```python
from billing_system import BillingSystem, Item

from billing_system.payment.stripe_gateway import StripeGateway

## Initialize the billing system

stripe_gateway = StripeGateway("your_stripe_api_key")
billing_system = BillingSystem()

# Register vendors
electronics_vendor = billing_system.register_vendor("Electronics Store")

# Create an order
order = billing_system.create_order()

# Add items
billing_system.add_item_to_order(order, 
    Item(item_id="laptop001", name="Gaming Laptop", price=1200.00, vendor_id=electronics_vendor)
)

# Process payment
vendor_payments = billing_system.process_order_payment(order)
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
MIT License
```