# Copy the loop from "Square Roots" on page 79 and encapsulate it in a function called 'mysqrt' that takes 'a' as a
# parameter, chooses a reasonable value of x and returns an estimate of the square root of 'a'.
# To test it, write a function named 'test_square_root' that print a table like this:

# a   mysqrt(a)     math.sqrt(a)  diff
# 1.0 1.0           1.0           0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0
# 4.0 2.0           2.0           0.0
# 5.0 2.2360679775  2.2360679775  0.0
# 6.0 2.44948974278 2.44948974278 0.0
# 7.0 2.64575131106 2.64575131106 0.0
# 8.0 2.82842712475 2.82842712475 4.4408920985e-16
# 9.0 3.0           3.0           0.0

# The first column is a number 'a', the second column is the square root of 'a' computed with 'mysqrt', the third
# column is the square root computed by 'math.sqrt' and the fourth column is the absolute value of the difference
# between the two estimates.

import math


def mysqrt(a):
    """Find square root of 'a' and return 'x' using Newton's method"""
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            return x
        x = y


def test_square_root():
    """Find square root of all integers between 1 and 9 using 'mysqrt' and 'math.sqrt' function, compare the output and
    print a table with the output values."""
    header = "a   mysqrt(a)     math.sqrt(a)  diff"
    divider ="-   ---------     ------------  ----"
    print(header + "\n" + divider)

    a = 1
    for i in range(9):
        my_sqrt = mysqrt(a)
        math_sqrt = math.sqrt(a)
        diff = math_sqrt - my_sqrt

        row = f"{float(a)} {my_sqrt:.11f} {math_sqrt:.11f} {diff}"
        print(row)
        a += 1


test_square_root()


# Alternative using the 'abs' function with 'epsilon = 0.0000001'.
print("\n")


def mysqrt_abs(a):
    """Find square root of 'a' and return 'x' using Newton's method"""
    x = 3
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if abs(y-x) < epsilon:
            return x
        x = y


def test_square_root_abs():
    """Find square root of all integers between 1 and 9 using 'mysqrt' and 'math.sqrt' function, compare the output and
        print a table with the output values."""
    header = "a   mysqrt(a)     math.sqrt(a)  diff"
    divider ="-   ---------     ------------  ----"
    print(header + "\n" + divider)

    a = 1
    for i in range(9):
        my_sqrt = mysqrt_abs(a)
        math_sqrt = math.sqrt(a)
        diff = my_sqrt - math_sqrt

        row = f"{float(a)} {my_sqrt:.11f} {math_sqrt:.11f} {diff}"
        print(row)
        a += 1


test_square_root_abs()
