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


# Expanded solution that uses modified versions of the previous functions and turtle to draw a triangle.
import math, turtle


def is_triangle_2(a, b, c):
    """Check if a triangle can be formed with the given length for 'a', 'b' and 'c'."""
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


def draw_triangle(t):
    """Take user input for values 'a', 'b' and 'c', call 'is_triangle_2()' with these parameters. If return value is
    'True', draw a triangle. 't' is a turtle."""
    a = int(input("Enter length of stick 'a': "))
    b = int(input("Enter length of stick 'b': "))
    c = int(input("Enter length of stick 'c': "))

    if is_triangle_2(a, b, c):
        angle_a = 180 - math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_b = 180 - math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_c = 180 - math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        t.fd(a)
        t.lt(angle_c)
        t.fd(b)
        t.lt(angle_a)
        t.fd(c)
        t.lt(angle_b)  # Not really necessary. Only used to point the turtle back into it's starting orientation.
    else:
        print("That doesn't work.")


triangle = turtle.Turtle()
draw_triangle(triangle)

turtle.mainloop()
