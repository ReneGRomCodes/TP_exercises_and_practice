# Imports for this set of exercises.
import turtle
import math


# 4-2: Write an appropriately general set of functions that can draw flowers as in Figure 4-1 (refer to book).


# 4-3: Write an appropriately general set of functions that can draw figures as in Figure 4-2 (refer to book).

shape = turtle.Turtle()


def draw_triangle(t, a, angle_a):
    """Draw an isosceles triangle with leg length 'a' and apex angle 'angle_a'. 't' is a turtle."""
    base = 2 * a * math.sin(math.radians(angle_a) / 2)
    angle_base = 180 - ((180 - angle_a) / 2)
    t.fd(a)
    t.lt(angle_base)
    t.fd(base)
    t.lt(angle_base)
    t.fd(a)


def draw_shape(t, r, n_sides):
    """Take radius 'r' and number of sides 'n_sides' to draw a polygon. 't' is a turtle."""
    for i in range(n_sides):
        draw_triangle(t, r, 360/n_sides)
        t.lt(180)


# draw_shape(shape, 150, 7)


# 4-4: The letters of the alphabet can be constructed from a moderate number of basic elements, like vertical and
# horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and
# then write functions that draw the letters.
# You should write one function for each letter with names 'draw_a', 'draw_b', etc. and put your functions.


# 4-5: Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write a program draws an Archimedian spiral.


turtle.mainloop()
