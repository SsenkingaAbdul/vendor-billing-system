from typing import Dict
from ..models import Order

class TaxCalculator:
    def __init__(self, tax_rates: Dict[str, float]):
        self.tax_rates = tax_rates  # region: rate
        
    def calculate_tax(self, order: Order, region: str) -> float:
        if region not in self.tax_rates:
            raise ValueError(f"No tax rate defined for region: {region}")
            
        return order.total_amount * self.tax_rates[region] 