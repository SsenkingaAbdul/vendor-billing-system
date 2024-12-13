import unittest
from src.billing_system.exceptions import (
    BillingSystemError,
    VendorNotRegisteredError,
    EmptyOrderError
)

class TestExceptions(unittest.TestCase):
    def test_billing_system_error(self):
        """Test base exception"""
        with self.assertRaises(BillingSystemError):
            raise BillingSystemError("Test error")

    def test_vendor_not_registered_error(self):
        """Test vendor not registered error"""
        with self.assertRaises(VendorNotRegisteredError):
            raise VendorNotRegisteredError("Vendor not found")

    def test_empty_order_error(self):
        """Test empty order error"""
        with self.assertRaises(EmptyOrderError):
            raise EmptyOrderError("Order is empty")

    def test_exception_inheritance(self):
        """Test exception inheritance"""
        self.assertTrue(issubclass(VendorNotRegisteredError, BillingSystemError))
        self.assertTrue(issubclass(EmptyOrderError, BillingSystemError))

if __name__ == '__main__':
    unittest.main() 