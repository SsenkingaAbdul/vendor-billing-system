import unittest
from src.billing_system.models import Item, Order

class TestItem(unittest.TestCase):
    def test_item_creation(self):
        """Test item initialization"""
        item = Item(
            item_id="test001",
            name="Test Item",
            price=100.00,
            vendor_id="vendor001"
        )
        self.assertEqual(item.item_id, "test001")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 100.00)
        self.assertEqual(item.vendor_id, "vendor001")

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        """Test order initialization"""
        order = Order(customer_id="customer001")
        self.assertIsNotNone(order.order_id)
        self.assertEqual(order.customer_id, "customer001")
        self.assertEqual(order.total_amount, 0.0)
        self.assertEqual(len(order.items), 0)
        self.assertEqual(len(order.vendor_payments), 0)

    def test_order_with_items(self):
        """Test order with added items"""
        order = Order(customer_id="customer001")
        item = Item(
            item_id="test001",
            name="Test Item",
            price=100.00,
            vendor_id="vendor001"
        )
        order.items.append(item)
        order.total_amount += item.price
        
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.total_amount, 100.00)

if __name__ == '__main__':
    unittest.main() 