# Imports for this set of exercises.
import turtle
import math


# 4-2: Write an appropriately general set of functions that can draw flowers as in Figure 4-1 (refer to book).

def arc(t, r, angle):
    """Draw an arc length 'angle' from a circle with radius 'r'. 't' is a turtle."""
    step = (2 * math.pi * r) / 360
    for i in range(angle):
        t.fd(step)
        t.lt(1)


def draw_flower(t, n_petals, len_petals, angle):
    """Draw a flower pattern with number of petals 'n_petals', length of petals 'len_petals' and width of the petal
    'angle'. 't' is a turtle."""
    for i in range(n_petals):
        for i in range(2):
            arc(t, len_petals, angle)
            t.lt(180 - angle)
        t.lt(360 / n_petals)


# flower = turtle.Turtle()
# draw_flower(flower, 7, 200, 30)


# 4-3: Write an appropriately general set of functions that can draw figures as in Figure 4-2 (refer to book).

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


# shape = turtle.Turtle()
# draw_shape(shape, 150, 7)


# 4-4: The letters of the alphabet can be constructed from a moderate number of basic elements, like vertical and
# horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and
# then write functions that draw the letters.
# You should write one function for each letter with names 'draw_a', 'draw_b', etc. and put your functions.


# Letters will be constructed within imaginary blocks made up of two squares on top of each other.

# Length of the side of a square. Changing this value will change the scale of the letters.
len_line = 40
# Diagonal from one corner of a square to the opposite corner.
len_diagonal_1 = math.sqrt((len_line**2) * 2)
# Diagonal from one corner of a square to the middle of the opposite side and it's angles.
len_diagonal_2 = math.sqrt(len_line**2 + (len_line / 2)**2)
angle_ac = 26.57
angle_bc = 63.43


def semicircle(t, r=len_line/2):
    """Draw a semicircle within one square using 'len_line/2' as default radius 'r'. 't' is a turtle."""
    n_sides = 50
    length_sides = (2 * math.pi * r) / n_sides
    n_arc_sides = int(n_sides / 360 * 180)

    for i in range(n_arc_sides):
        t.fd(length_sides)
        t.lt(360 / n_sides)

    t.fd(length_sides)


def quarter_circle(t, r=len_line):
    """Draw a quarter circle within one square using 'len_line' as default radius 'r'. 't' is a turtle."""
    n_sides = 50
    length_sides = (2 * math.pi * r) / n_sides
    n_arc_sides = int(n_sides / 360 * 90)

    for i in range(n_arc_sides + 1):
        t.fd(length_sides)
        t.lt(360 / n_sides)


# Skipped mostly. The following functions are examples on how to use the variables and functions above.

def draw_b(t):
    semicircle(t)
    t.lt(180)
    semicircle(t)
    t.lt(90)
    t.fd(len_line * 2)
    # Turning turtle back into starting position.
    t.lt(90)


def draw_c(t):
    # Bring turtle into correct starting position so that it occupies the same space as other letters.
    t.pu()
    t.lt(angle_bc)
    t.fd(len_diagonal_2 * 2)
    t.pd()
    # Start drawing the actual letter.
    t.lt(90 + angle_ac)
    quarter_circle(t)
    quarter_circle(t)
    # Turning turtle back into starting position.
    t.rt(360 / 50)


def draw_r(t):
    t.lt(90)
    t.fd(len_line)
    t.rt(90)
    semicircle(t)
    t.lt(90)
    t.fd(len_line)
    t.lt(angle_ac)
    t.fd(len_diagonal_2)
    # Moving turtle back into starting position.
    t.pu()
    t.rt(180 - angle_bc)
    t.fd(len_line / 2)
    t.lt(180)
    t.pd()


# letter = turtle.Turtle()
# draw_b(letter)
# draw_c(letter)
# draw_r(letter)


# 4-5: Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write a program draws an Archimedian spiral.

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draw an Archimedian spiral.

    Args:
        n: how many line segments to draw
        length: how long each segment is
        a: how loose the initial spiral
            starts out (larger is looser)
        b: how loosely coiled the spiral is
            (larger is looser)
        t: turtle
    """

    theta = 0.0
    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta


# spiral = turtle.Turtle()
# draw_spiral(spiral, 1000, 2, 0.2, 0.002)

turtle.mainloop()
