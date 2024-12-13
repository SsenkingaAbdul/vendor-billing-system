import uuid
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

@dataclass
class Item:
    name: str
    price: float
    vendor_id: str
    quantity: int = 1
    item_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    def total_price(self) -> float:
        return self.price * self.quantity

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class OrderHistory:
    timestamp: datetime
    status: OrderStatus
    message: str

@dataclass
class Order:
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[Item] = field(default_factory=list)
    total_amount: float = 0.0
    vendor_payments: Dict[str, float] = field(default_factory=dict)
    status: OrderStatus = field(default=OrderStatus.PENDING)
    created_at: datetime = field(default_factory=datetime.now)
    history: List[OrderHistory] = field(default_factory=list)
    
    def update_status(self, status: OrderStatus, message: Optional[str] = None):
        self.status = status
        self.history.append(OrderHistory(
            timestamp=datetime.now(),
            status=status,
            message=message or ""
        ))