import uuid
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Item:
    """
    Represents a single item in an order.
    
    Attributes:
    - item_id: Unique identifier for the item
    - name: Name of the item
    - price: Price of the item
    - vendor_id: ID of the vendor selling the item
    """
    item_id: str
    name: str
    price: float
    vendor_id: str

@dataclass
class Order:
    """
    Represents a customer's complete order.
    
    Attributes:
    - order_id: Unique identifier for the order
    - items: List of items in the order
    - customer_id: ID of the customer placing the order
    - total_amount: Total cost of the order
    - vendor_payments: Distribution of payments to vendors
    """
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[Item] = field(default_factory=list)
    customer_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    total_amount: float = 0.0
    vendor_payments: Dict[str, float] = field(default_factory=dict)