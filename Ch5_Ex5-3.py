# If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the
# sticks is 12 inches longs and the other two are one inch long, you will not be able to get the short sticks to meet
# in the middle.

# 1. Write a function named 'is_triangle' that takes three integers as arguments and prints either "Yes" or "No",
# depending on whether you can or cannot form a triangle from sticks with the given length.

def is_triangle(a, b, c):
    """Check if a triangle can be formed with the given length for 'a', 'b' and 'c'."""
    if a + b > c and b + c > a and a + c > b:
        print("Yes")
    else:
        print("No")


# 2. Write a function that prompts the user to input three stick lengths, converts them to integers and uses
# 'is_triangle' to check whether the sticks with the given lengths can form a triangle.

def is_triangle_input():
    """Take user input for values 'a', 'b' and 'c' and call 'is_triangle()' with these parameters."""
    a = int(input("Enter length of stick 'a': "))
    b = int(input("Enter length of stick 'b': "))
    c = int(input("Enter length of stick 'c': "))

    is_triangle(a, b, c)
