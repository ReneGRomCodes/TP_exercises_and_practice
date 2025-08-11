# Exercise 15-1: Write a definition for a class named 'Circle' with attributes 'center' and 'radius', where center is a
# Point object and radius is a number.
# 1. Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
# 2. Write a function named 'point_in_circle()' that takes a Circle and a Point and returns 'True' if the Point lies in or
#    on the boundary of the circle.
# 3. Write a function named 'rect_in_circle()' that takes a Circle and a Rectangle and returns 'True' if the Rectangle lies
#    entirely in or on the boundary of the circle.
# 4. Write a function named 'rect_circle_overlap()' that takes a Circle and a Rectangle and return 'True' if any of the
#    corners of the Rectangle fall inside the circle. Or as a more challenging version, return 'True' if any part of the
#    Rectangle falls inside the circle.
import math


class Point:
    """Represents a point in 2-D space."""

class Circle:
    """Represents a circle"""

class Rect:
    """Represent a rectangle"""

# 1.
circle = Circle()
circle.center = Point()
circle.center.x, circle.center.y = (150, 100)
circle.radius = 75

# 2.
def point_in_circle(circle_object, point_object):
    """Take a point and return True if it is within a circle.
    ARGS:
        circle_object: instance of class Circle.
        point_object: instance of class Point.
    RETURNS:
        Bool
    """
    distance_to_center = math.sqrt((point_object.x - circle_object.center.x)**2 +
                                   (point_object.y - circle_object.center.y)**2)

    if distance_to_center <= circle_object.radius:
        return True
    else:
        return False

# 3.
rect = Rect()
rect.center = circle.center
rect.a = 50
rect.b = 70

def rect_in_circle(circle_object, rect_object):
    """Take a rect object and return True if it is within entirely within a circle, assuming both share the same center
    point.
    ARGS:
        circle_object: instance of class Circle.
        rect_object: instance of class Rect.
    RETURNS:
        bool
    """
    rect_corner_pos = (rect_object.center.x + (rect_object.a / 2),
                       rect_object.center.y + (rect_object.b / 2))

    distance_corner = math.sqrt((rect_object.center.x - rect_corner_pos[0])**2 +
                                (rect_object.center.y - rect_corner_pos[1])**2)

    if distance_corner <= circle_object.radius:
        return True
    else:
        return False

# 4.
def rect_circle_overlap(circle_object, rect_object):
    """Take a rect object and return True if it is at least partially within a circle.
    ARGS:
        circle_object: instance of class Circle.
        rect_object: instance of class Rect.
    RETURNS:
        bool
    """
    corner_a = (rect_object.center.x + (rect_object.a / 2), rect_object.center.y + (rect_object.b / 2))
    corner_b = (rect_object.center.x + (rect_object.a / 2), rect_object.center.y - (rect_object.b / 2))
    corner_c = (rect_object.center.x - (rect_object.a / 2), rect_object.center.y + (rect_object.b / 2))
    corner_d = (rect_object.center.x - (rect_object.a / 2), rect_object.center.y - (rect_object.b / 2))
    corners = (corner_a, corner_b, corner_c, corner_d)

    for corner in corners:
        corner_object = Point()
        corner_object.x, corner_object.y = corner[0], corner[1]

        if point_in_circle(circle_object, corner_object):
            return True

    return False


# Alternative class definitions (with use of __init__() method) and instances... the proper way ;)
class AltPoint:
    """Represents a point in 2-D space."""
    def __init__(self, coords):
        """Initialize class attributes.
        ARGS:
            coords: list or tuple containing x and y values.
        """
        self.x = coords[0]
        self.y = coords[1]

class AltCircle:
    """Represents a circle."""
    def __init__(self, center, radius):
        """Initialize class attributes.
        ARGS:
            center: list or tuple with x and y values for center point.
            radius: int for circle radius.
        """
        self.center = AltPoint(center)
        self.radius = radius

class AltRect:
    """Represent a rectangle"""
    def __init__(self, side_lengths, center):
        """Initialize class attributes.
        ARGS:
            side_lengths: list or tuple with values for sides a and b.
            center: list or tuple with x and y values for center point.
        """
        self.a = side_lengths[0]
        self.b = side_lengths[1]
        self.center = center

alt_circle = AltCircle((150, 100), 75)
alt_rect = AltRect((50, 70), alt_circle.center)


# Exercise 15-2: Write a function called 'draw_rect()' that takes a Turtle object and a Rectangle and uses the Turtle do
# draw the Rectangle.
# Write a function called 'draw_circle()' that takes a Turtle and a circle and draws the Circle.
import turtle


t_rect = Rect()
t_rect.a = 50
t_rect.b = 70

def draw_rect(rectangle):
    """Draw a Rect object 'rectangle' on screen using a turtle.
    ARGS:
        rectangle: instance of class Rect.
    """
    t = turtle.Turtle()

    for _ in range(2):
        t.fd(rectangle.a)
        t.lt(90)
        t.fd(rectangle.b)
        t.lt(90)


t_circle = Circle()
t_circle.radius = 75

def draw_circle(circ):
    """Draw a Circle object 'circ' on screen using a turtle.
    ARGS:
        circ: instance of class Circle.
    """
    t = turtle.Turtle()

    circumference = 2 * math.pi * circ.radius
    n = int(circumference / 3) + 1
    length = circumference / n
    angle = 360 / n

    for _ in range(n):
        t.fd(length)
        t.lt(angle)
