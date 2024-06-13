# A number 'a' is a power of 'b' if it is divisible by 'b' and 'a / b' is a power of 'b'. Write a function called
# 'is_power' that takes parameters 'a' and 'b' and returns 'True' if 'a' is a power of 'b'. Note: you will have to think
# about the base case.

def is_power(a, b):
    """Return 'True' if 'a' is a power of 'b'."""
    if a/b == 1:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False


print(is_power(81, 3))  # True
print(is_power(16, 2))  # True
print(is_power(20, 3))  # False
print(is_power(18, 2))  # False
