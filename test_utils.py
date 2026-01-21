"""Unit tests for utils module."""

import pytest
from utils import calculate_total, validate_email, process_user_data


class TestCalculateTotal:
    """Tests for calculate_total function."""
    
    def test_empty_list(self):
        """Test with empty list."""
        assert calculate_total([]) == 0
    
    def test_single_item(self):
        """Test with single item."""
        assert calculate_total([5]) == 5
    
    def test_multiple_items(self):
        """Test with multiple items."""
        assert calculate_total([1, 2, 3, 4, 5]) == 15


class TestValidateEmail:
    """Tests for validate_email function."""
    
    def test_valid_email(self):
        """Test with valid email."""
        assert validate_email("user@example.com") is True
    
    def test_invalid_email_no_at(self):
        """Test with email missing @."""
        assert validate_email("user.example.com") is False
    
    def test_invalid_email_no_dot(self):
        """Test with email missing dot."""
        assert validate_email("user@example") is False


class TestProcessUserData:
    """Tests for process_user_data function."""
    
    def test_process_user_data(self):
        """Test processing user data."""
        user = {
            'name': 'John Doe',
            'age': 30,
            'email': 'john@example.com'
        }
        result = process_user_data(user)
        
        assert result['name'] == 'JOHN DOE'
        assert result['age'] == 30
        assert result['email'] == 'john@example.com'

if __name__ == "__main__":
    pytest.main()