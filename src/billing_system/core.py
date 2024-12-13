import uuid
from typing import List, Dict
from .models import Item, Order
from .exceptions import VendorNotRegisteredError, EmptyOrderError

class BillingSystem:
    """
    Manages the billing process for multiple vendors and customers.
    
    Handles order creation, item addition, and payment distribution.
    """
    
    def __init__(self):
        """
        Initialize the billing system with empty vendor and order registries.
        """
        self.vendors: Dict[str, str] = {}  # vendor_id: vendor_name
        self.orders: Dict[str, Order] = {}
    
    def register_vendor(self, vendor_name: str) -> str:
        """
        Register a new vendor in the system.
        
        Args:
            vendor_name: Name of the vendor to register
        
        Returns:
            Unique vendor ID
        """
        vendor_id = str(uuid.uuid4())
        self.vendors[vendor_id] = vendor_name
        return vendor_id
    
    def create_order(self, customer_id: str = None) -> Order:
        """
        Create a new order for a customer.
        
        Args:
            customer_id: Optional customer ID. If not provided, a new one is generated
        
        Returns:
            A new Order object
        """
        order = Order(customer_id=customer_id or str(uuid.uuid4()))
        self.orders[order.order_id] = order
        return order
    
    def add_item_to_order(self, order: Order, item: Item) -> None:
        """
        Add an item to an existing order.
        
        Args:
            order: The order to add the item to
            item: The item to be added
        
        Raises:
            VendorNotRegisteredError if the vendor is not registered
        """
        if item.vendor_id not in self.vendors:
            raise VendorNotRegisteredError(f"Vendor {item.vendor_id} is not registered")
        
        order.items.append(item)
        order.total_amount += item.price
    
    def calculate_vendor_payments(self, order: Order) -> Dict[str, float]:
        """
        Calculate payment distribution for vendors in an order.
        
        Args:
            order: The order to calculate payments for
        
        Returns:
            A dictionary of vendor IDs and their corresponding payment amounts
        """
        vendor_payments = {}
        for item in order.items:
            if item.vendor_id not in vendor_payments:
                vendor_payments[item.vendor_id] = 0.0
            vendor_payments[item.vendor_id] += item.price
        
        order.vendor_payments = vendor_payments
        return vendor_payments
    
    def process_order_payment(self, order: Order) -> Dict[str, float]:
        """
        Process the payment for an entire order.
        
        Args:
            order: The order to process payment for
        
        Returns:
            A dictionary showing payment distribution to vendors
        
        Raises:
            EmptyOrderError if the order has no items
        """
        if not order.items:
            raise EmptyOrderError("Cannot process an empty order")
        
        vendor_payments = self.calculate_vendor_payments(order)
        return vendor_payments