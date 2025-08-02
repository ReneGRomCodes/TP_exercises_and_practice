# The greatest common divisor (GCD) of 'a' and 'b' is the largest number that divides both of them with no remainder.
# One way to find the GCD of two numbers is base on the observation that if 'r' is the remainder when 'a' is divided by
# 'b', then 'gcd(a,b) = gcd(b,r)'. As a base case, we can use 'gcd(a,0) = a'.
# Write a function called 'gcd' that takes parameters 'a' and 'b' and returns their GCD.

def gcd(a, b):
    """Return greatest common divisor of 'a' and 'b'."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))  # GCD is 6
print(gcd(81, 27))  # GCD is 27
print(gcd(56, 42))  # GCD is 14
print(gcd(105, 35))  # GCD is 35
