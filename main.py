"""Main application entry point."""

from models import User, Product
from utils import calculate_total, validate_email, process_user_data


def main():
    """Main function."""
    print("Welcome to Demo App for Qodo Merge Testing!")
    
    # Create a user
    user = User("John Doe", "john@example.com", 25)
    print(f"User: {user.get_display_name()}")
    print(f"Is Adult: {user.is_adult()}")
    
    # Create products
    products = [
        Product("Laptop", 999.99, 10),
        Product("Mouse", 29.99, 50),
        Product("Keyboard", 79.99, 25),
    ]
    
    # Calculate total inventory value
    total_value = sum(p.calculate_total_value() for p in products)
    print(f"\nTotal Inventory Value: ${total_value:.2f}")
    
    # Demo email validation
    test_emails = ["valid@email.com", "invalid.email", "test@domain.co.uk"]
    for email in test_emails:
        is_valid = validate_email(email)
        print(f"Email '{email}' is valid: {is_valid}")


if __name__ == "__main__":
    main()