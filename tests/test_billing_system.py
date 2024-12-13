import pytest
from src.billing_system import BillingSystem, Item, VendorNotRegisteredError, EmptyOrderError

def test_vendor_registration():
    billing_system = BillingSystem()
    vendor_id = billing_system.register_vendor("Test Vendor")
    assert vendor_id in billing_system.vendors
    assert billing_system.vendors[vendor_id] == "Test Vendor"

def test_order_creation():
    billing_system = BillingSystem()
    order = billing_system.create_order()
    assert order.order_id in billing_system.orders

def test_add_item_to_order():
    billing_system = BillingSystem()
    vendor_id = billing_system.register_vendor("Test Vendor")
    order = billing_system.create_order()
    
    item = Item(item_id="test001", name="Test Item", price=100.00, vendor_id=vendor_id)
    billing_system.add_item_to_order(order, item)
    
    assert len(order.items) == 1
    assert order.total_amount == 100.00

def test_vendor_not_registered():
    billing_system = BillingSystem()
    order = billing_system.create_order()
    
    item = Item(item_id="test001", name="Test Item", price=100.00, vendor_id="invalid_vendor")
    
    with pytest.raises(VendorNotRegisteredError):
        billing_system.add_item_to_order(order, item)

def test_process_empty_order():
    billing_system = BillingSystem()
    order = billing_system.create_order()
    
    with pytest.raises(EmptyOrderError):
        billing_system.process_order_payment(order)

def test_vendor_payment_calculation():
    billing_system = BillingSystem()
    vendor1 = billing_system.register_vendor("Vendor 1")
    vendor2 = billing_system.register_vendor("Vendor 2")
    
    order = billing_system.create_order()
    
    item1 = Item(item_id="item1", name="Item 1", price=100.00, vendor_id=vendor1)
    item2 = Item(item_id="item2", name="Item 2", price=50.00, vendor_id=vendor2)
    
    billing_system.add_item_to_order(order, item1)
    billing_system.add_item_to_order(order, item2)
    
    vendor_payments = billing_system.process_order_payment(order)
    
    assert vendor_payments[vendor1] == 100.00
    assert vendor_payments[vendor2] == 50.00