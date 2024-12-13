class BillingSystemError(Exception):
    """Base exception for billing system errors."""
    pass

class VendorNotRegisteredError(BillingSystemError):
    """Raised when an unregistered vendor is attempted to be used."""
    pass

class EmptyOrderError(BillingSystemError):
    """Raised when attempting to process an empty order."""
    pass