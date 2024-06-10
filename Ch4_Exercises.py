# Imports for this set of exercises
import turtle
import math

# 1. Write a function called 'square' that takes a parameter named 't', which is a turtle. It should use the turtle to
# draw a square.
# Write a function that passes 'bob' as an argument to 'square' and then run the program again.

bob = turtle.Turtle()  # Used for all exercises.


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


# square(bob)


# 2. Add another parameter, named 'length' to square. Modify the body so length of the sides is 'length' and then modify
# the function call to provide a second argument. Run the program again. Test your program with a range of values for
# length.

def square_2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square_2(bob, 200)


# 3. Make a copy of square and change the name to 'polygon'. Add another parameter named 'n' and modify the body, so it
# draws an n_sided regular polygon.

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


# polygon(bob, 100, 6)


# 4. Write a function called 'circle' that takes a turtle 't' and radius 'r' as parameters and draw an approximate
# circle by calling 'polygon' with an appropriate length and number of sides. Test your function with a range of values
# for 'r'.

def circle(t, r):
    n_sides = 200
    length_sides = (2 * math.pi * r) / n_sides
    for i in range(n_sides):
        t.fd(length_sides)
        t.lt(360 / n_sides)


# circle(bob, 100)


# 5. Make a more general version of 'circle' called 'arc' that takes an additional parameter 'angle', which determines
# what fraction of a circle to draw. 'angle' is in units of degrees, so when 'angle=360', 'arc' should draw a complete
# circle.

def arc(t, r, angle):
    n_sides = 200
    length_sides = (2 * math.pi * r) / n_sides
    n_arc_sides = int(n_sides / 360 * angle)

    for i in range(n_arc_sides):
        t.fd(length_sides)
        t.lt(360 / n_sides)


# arc(bob, 100, 90)


# Expanded function printing a pie slice of the circle.

def pie(t, r, angle):
    n_sides = 200
    length_sides = (2 * math.pi * r) / n_sides
    n_arc_sides = int(n_sides / 360 * angle)  # Converted to integer for use as argument in 'for loop'.

    t.fd(r)
    t.lt(90)
    for i in range(n_arc_sides):
        t.fd(length_sides)
        t.lt(360 / n_sides)
    t.lt(90)
    t.fd(r)


# pie(bob, 200, 35)


turtle.mainloop()
