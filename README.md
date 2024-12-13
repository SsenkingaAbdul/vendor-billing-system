# Vendor Billing System

## Overview
A flexible Python library for managing multi-vendor billing and order processing.

## Features
- Register multiple vendors
- Create and manage customer orders
- Add items from different vendors
- Automatic payment distribution
- Comprehensive error handling

## Installation
```bash
pip install vendor-billing-system
```

## Quick Start
```python
from billing_system import BillingSystem, Item

# Initialize the billing system
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