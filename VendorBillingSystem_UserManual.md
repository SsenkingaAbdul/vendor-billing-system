# Vendor Billing System
## User Manual
### Version 1.0.0

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [System Requirements](#system-requirements)
4. [Getting Started](#getting-started)
5. [Core Features](#core-features)
6. [Advanced Usage](#advanced-usage)
7. [Troubleshooting](#troubleshooting)
8. [API Reference](#api-reference)

## 1. Introduction
The Vendor Billing System is a flexible Python library designed for managing multi-vendor billing and order processing. It supports multiple payment gateways, shipping calculations, and comprehensive order management.

### Key Features
- Multi-vendor support
- Multiple payment gateway integration (Stripe, PayPal)
- Shipping calculation
- Order management
- Automatic payment distribution
- Discount handling

## 2. Installation

### Using pip 
```bash
pip install vendor-billing-system
```

### From source
```bash
git clone https://github.com/SsenkingaAbdul/vendor-billing-system.git
cd vendor-billing-system
pip install -e .
```

## 3. System Requirements
- Python 3.8 or higher
- Required dependencies:
  - pydantic>=2.0.0
  - stripe>=5.0.0
  - sqlalchemy>=2.0.0

## 4. Getting Started

### Basic Usage Example
```python
from billing_system import BillingSystem, Item
from billing_system.payment.stripe_gateway import StripeGateway

# Initialize the system
stripe_gateway = StripeGateway("your_stripe_api_key")
billing_system = BillingSystem(payment_gateway=stripe_gateway)

# Register a vendor
vendor_id = billing_system.register_vendor("Example Store")

# Create an order
order = billing_system.create_order()

# Add items
item = Item(
    name="Product",
    price=99.99,
    vendor_id=vendor_id,
    quantity=1
)
billing_system.add_item_to_order(order, item)

# Process payment
result = billing_system.process_order_payment(
    order,
    payment_details={"payment_method_id": "pm_card_visa"}
)
```

## 5. Core Features

### 5.1 Vendor Management
```python
# Register vendors
vendor_id = billing_system.register_vendor("Vendor Name")
```

### 5.2 Order Management
```python
# Create order
order = billing_system.create_order()

# Add items
billing_system.add_item_to_order(order, item)
```

### 5.3 Payment Processing
```python
# Process payment
result = billing_system.process_order_payment(order, payment_details)
```

### 5.4 Shipping Calculation
```python
from billing_system.shipping.address import ShippingAddress
from billing_system.shipping.calculator import ShippingCalculator

address = ShippingAddress(
    street="123 Main St",
    city="Example City",
    state="EX",
    country="US",
    postal_code="12345"
)

shipping_cost = shipping_calculator.calculate_shipping(order, address)
```

## 6. Advanced Usage

### 6.1 Custom Payment Gateways
```python
from billing_system.payment.base import PaymentGateway

class CustomGateway(PaymentGateway):
    def process_payment(self, order, payment_details):
        # Implementation
        pass
```

### 6.2 Discount Systems
```python
from billing_system.pricing.discounts import PercentageDiscount

discount = PercentageDiscount(percentage=10)
final_price = discount.apply_discount(order)
```

## 7. Troubleshooting

### Common Issues and Solutions

#### Issue: Payment Processing Failed
```python
try:
    result = billing_system.process_order_payment(order, payment_details)
except Exception as e:
    print(f"Payment failed: {str(e)}")
```

#### Issue: Invalid Shipping Address
```python
if not address.is_valid():
    print("Please provide a valid shipping address")
```

## 8. API Reference

### BillingSystem Class
```python
class BillingSystem:
    def __init__(self, 
                 payment_gateway=None,
                 shipping_calculator=None):
        """Initialize billing system"""
        
    def register_vendor(self, vendor_name: str) -> str:
        """Register a new vendor"""
        
    def create_order(self) -> Order:
        """Create a new order"""
        
    def add_item_to_order(self, order: Order, item: Item):
        """Add item to order"""
        
    def process_order_payment(self, order: Order, 
                            payment_details: dict) -> dict:
        """Process payment for order"""
```

### Item Class
```python
@dataclass
class Item:
    name: str
    price: float
    vendor_id: str
    quantity: int = 1
```

### Order Class
```python
@dataclass
class Order:
    order_id: str
    items: List[Item]
    total_amount: float
    status: OrderStatus
```

## Support and Contact
For support inquiries, please contact:
- Email: abdulssenkinga21@gmail.com
- GitHub Issues: https://github.com/SsenkingaAbdul/vendor-billing-system/issues

## License
This project is licensed under the MIT License. See the LICENSE file for details.

