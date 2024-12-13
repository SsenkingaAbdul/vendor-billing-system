from abc import ABC, abstractmethod
from ..models import Order

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order: Order) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage
        
    def apply_discount(self, order: Order) -> float:
        return order.total_amount * (1 - self.percentage / 100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, item_threshold: int, discount_percentage: float):
        self.item_threshold = item_threshold
        self.discount_percentage = discount_percentage
        
    def apply_discount(self, order: Order) -> float:
        if len(order.items) >= self.item_threshold:
            return order.total_amount * (1 - self.discount_percentage / 100)
        return order.total_amount 