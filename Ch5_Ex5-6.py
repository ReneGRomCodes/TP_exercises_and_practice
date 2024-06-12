# The Koch curve is a fractal that looks something like Figure 5-2 (see book). To draw a Koch curve with length x, all
# you have to do is:

# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.
# Turn right 120 degrees.
# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.

# The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

import turtle

k_curve = turtle.Turtle()


# 1. Write a function called 'koch' that takes a turtle and a length as parameters and that uses the turtle to draw a
# Koch curve with the given length.

def koch(t, x):
    """Draw a Koch curve with length 'x'. 't' is a turtle."""
    length = x / 3

    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.lt(60)
    t.fd(length)


# 2. Write a function 'snowflake' that draws three Koch curves to make the outline of a snowflake.

def snowflake(t, x):
    """Draw a snowflake using 3 Koch curves with length 'x'. 't' is a turtle."""
    for i in range(3):
        koch(t, x)
        t.rt(120)


turtle.mainloop()
