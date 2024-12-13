import uuid
from typing import List, Dict, Optional
from .models import Item, Order
from .exceptions import VendorNotRegisteredError, EmptyOrderError
from .payment.base import PaymentGateway
from .pricing.discounts import DiscountStrategy
from .pricing.tax import TaxCalculator
from .shipping.calculator import ShippingCalculator
from .notifications.base import NotificationService
from .shipping.address import ShippingAddress

class BillingSystem:
    """
    Manages the billing process for multiple vendors and customers.
    
    Handles order creation, item addition, and payment distribution.
    """
    
    def __init__(self, 
                 payment_gateway: Optional[PaymentGateway] = None,
                 discount_strategy: Optional[DiscountStrategy] = None,
                 tax_calculator: Optional[TaxCalculator] = None,
                 shipping_calculator: Optional[ShippingCalculator] = None,
                 notification_service: Optional[NotificationService] = None):
        """
        Initialize the billing system with empty vendor and order registries.
        """
        self.vendors: Dict[str, str] = {}  # vendor_id: vendor_name
        self.orders: Dict[str, Order] = {}
        self.payment_gateway = payment_gateway
        self.discount_strategy = discount_strategy
        self.tax_calculator = tax_calculator
        self.shipping_calculator = shipping_calculator
        self.notification_service = notification_service
    
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
    
    def create_order(self) -> Order:
        """
        Create a new order for a customer.
        
        Returns:
            A new Order object
        """
        order = Order()
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
        order.vendor_payments[item.vendor_id] = order.vendor_payments.get(item.vendor_id, 0) + item.price
    
    def process_order_payment(self, order: Order, payment_details: Dict = None) -> Dict:
        """
        Process the payment for an entire order.
        
        Args:
            order: The order to process payment for
            payment_details: Optional payment details
        
        Returns:
            A dictionary showing payment distribution to vendors
        
        Raises:
            EmptyOrderError if the order has no items
        """
        if not order.items:
            raise EmptyOrderError("Cannot process payment for empty order")
            
        if self.payment_gateway and payment_details:
            return self.payment_gateway.process_payment(order, payment_details)
            
        return order.vendor_payments
    
    def calculate_final_price(self, order: Order, shipping_address: ShippingAddress) -> float:
        subtotal = order.total_amount
        
        if self.discount_strategy:
            subtotal = self.discount_strategy.apply_discount(order)
            
        if self.tax_calculator:
            tax = self.tax_calculator.calculate_tax(order, shipping_address.state)
            subtotal += tax
            
        if self.shipping_calculator:
            shipping = self.shipping_calculator.calculate_shipping(order, shipping_address)
            subtotal += shipping
            
        return subtotal