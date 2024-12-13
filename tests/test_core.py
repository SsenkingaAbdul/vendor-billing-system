import unittest
from src.billing_system.core import BillingSystem
from src.billing_system.models import Item, Order
from src.billing_system.exceptions import VendorNotRegisteredError, EmptyOrderError

class TestBillingSystem(unittest.TestCase):
    def setUp(self):
        """Initialize billing system before each test"""
        self.billing_system = BillingSystem()
        self.vendor_id = self.billing_system.register_vendor("Test Vendor")

    def test_vendor_registration(self):
        """Test vendor registration functionality"""
        vendor_name = "Electronics Store"
        vendor_id = self.billing_system.register_vendor(vendor_name)
        self.assertIn(vendor_id, self.billing_system.vendors)
        self.assertEqual(self.billing_system.vendors[vendor_id], vendor_name)

    def test_order_creation(self):
        """Test order creation"""
        order = self.billing_system.create_order()
        self.assertIsInstance(order, Order)
        self.assertIn(order.order_id, self.billing_system.orders)

    def test_add_item_to_order(self):
        """Test adding items to an order"""
        order = self.billing_system.create_order()
        item = Item(
            item_id="test001",
            name="Test Item",
            price=100.00,
            vendor_id=self.vendor_id
        )
        self.billing_system.add_item_to_order(order, item)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.total_amount, 100.00)

    def test_invalid_vendor(self):
        """Test adding item with invalid vendor"""
        order = self.billing_system.create_order()
        item = Item(
            item_id="test001",
            name="Test Item",
            price=100.00,
            vendor_id="invalid_vendor_id"
        )
        with self.assertRaises(VendorNotRegisteredError):
            self.billing_system.add_item_to_order(order, item)

    def test_empty_order_processing(self):
        """Test processing empty order"""
        order = self.billing_system.create_order()
        with self.assertRaises(EmptyOrderError):
            self.billing_system.process_order_payment(order)

if __name__ == '__main__':
    unittest.main() 