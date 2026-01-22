import pytest
from app import reverse_string

def test_reverse_basic():
    """Test a basic string reversal."""
    assert reverse_string("hello") == "olleh"

def test_reverse_palindrome():
    """Test that a palindrome remains the same."""
    assert reverse_string("madam") == "madam"

def test_reverse_empty():
    """Test handling of an empty string."""
    assert reverse_string("") == ""

def test_reverse_non_string_raises_error():
    """Ensure non-string inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a string"):
        reverse_string(12345)
