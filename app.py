def reverse_string(s):
    """Reverses the input string."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == "__main__":
    original = "CI Pipeline Lab"
    reversed_str = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")
