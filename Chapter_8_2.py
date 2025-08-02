# Write a one-line version of 'is_palindrome' from exercise 6-3.

def is_palindrome(s):
    """Take a string argument 's' and return 'True' if palindrome and 'False' if not."""
    return s == s[::-1]
