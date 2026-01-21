"""Data models for the application."""


class User:
    """User model."""
    
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def is_adult(self):
        """Check if user is an adult."""
        return self.age >= 18
    
    def get_display_name(self):
        """Get display name."""
        return f"{self.name} ({self.email})"


class Product:
    """Product model."""
    
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_value(self):
        """Calculate total value of product in inventory."""
        # Potential bug: no validation for negative prices
        return self.price * self.quantity
    
    def restock(self, amount):
        """Restock product."""
        # Bad practice: no parameter validation
        self.quantity += amount
    
    def sell(self, amount):
        """Sell product."""
        # Missing validation: doesn't check if quantity is sufficient
        self.quantity -= amount
        if self.quantity < 0:  # Only checks after deduction
            return False
        return True
