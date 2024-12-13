from dataclasses import dataclass

@dataclass
class ShippingAddress:
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    
    def is_valid(self) -> bool:
        return all([
            self.street,
            self.city,
            self.state,
            self.country,
            self.postal_code
        ])

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}" 