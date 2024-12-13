from decimal import Decimal
from typing import Dict
from ..models import Order
from .address import ShippingAddress

class ShippingCalculator:
    def __init__(self, rates: Dict[str, Dict[str, float]]):
        self.rates = rates  # country -> {service -> rate}
        
    def calculate_shipping(self, order: Order, address: ShippingAddress) -> float:
        if not address.is_valid():
            raise ValueError("Invalid shipping address")
            
        country_rates = self.rates.get(address.country)
        if not country_rates:
            raise ValueError(f"Shipping not available for country: {address.country}")
            
        base_rate = country_rates["base_rate"]
        per_item_rate = country_rates["per_item"]
        
        total_items = sum(item.quantity for item in order.items)
        return base_rate + (per_item_rate * total_items)