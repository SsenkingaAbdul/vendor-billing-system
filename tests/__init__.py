"""
Test suite for the Billing System package.

This package contains all test cases for the billing system components:
- Core billing system functionality
- Order management
- Vendor registration
- Payment processing
- Error handling
"""

# This file can be empty, as its presence marks the directory as a Python package.
# The docstring above is optional but helpful for documentation purposes.

# Import test modules to make them discoverable
from .test_billing_system import *
from .test_exceptions import *
from .test_core import *

# Version of the test suite
__version__ = "0.1.0"
