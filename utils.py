"""Utility functions for the application."""


def calculate_total(items):
    """Calculate total from items list."""
    total = 0
    for item in items:
        total = total + item  # Bad practice: should use sum()
    return total


def validate_email(email):
    """Validate email address."""
    # Potential bug: simple validation that might miss edge cases
    if "@" in email and "." in email:
        return True
    return False


def process_user_data(user_dict):
    """Process user data dictionary."""
    # Missing error handling
    name = user_dict['name']
    age = user_dict['age']
    email = user_dict['email']
    
    # Unused variable
    timestamp = None
    
    return {
        'name': name.upper(),
        'age': age,
        'email': email.lower()
    }


def get_user_info(user_id):
    """Fetch user information."""
    # Potential bug: no validation of user_id
    import requests
    
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    
    # Bad: directly accessing without status code check
    return response.json()

 asdasd xxx