# A palindrome is a word that is spelled the same backward and forward, like "noon" or "redivider"

# 2. Write a function called 'is_palindrome' that takes a string argument and returns 'True' if it is a palindrome and
# 'False' otherwise.

def is_palindrome(s):
    """Take a string argument 's' and return 'True' if palindrome and 'False' if not."""
    if s == s[::-1]:
        return True
    else:
        return False


# Not case-sensitive alternative using user input.
def is_palindrome_2():
    """Take user input string 's' and return 'True' if palindrome and 'False' if not."""
    s = input("Enter word to test for palindrome: ")
    if s.lower() == s.lower()[::-1]:
        return True
    else:
        return False
