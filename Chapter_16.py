# Exercise 16-1: Write a function called 'mul_time()' that takes a Time object and a number and returns a new Time object
# that contains the product of the original Time and number.
# Then use 'mul_time()' to write a function that takes a Time object that represents the finishing time in a race, and
# a number that represents the distance, and returns a Time object that represents the average pace (time per mile).
import copy

class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

time = Time()
time.hour = 0
time.minute = 0
time.second = 0

def mul_time(t, n):  # I know this one is not the most efficient way, but wanted to keep it as basic and readable as possible.
    """Multiply Time object with n and return new Time object containing the product.
    ARGS:
        t: instance of class Time.
        n: time in seconds.
    RETURNS:
        new_t: instance of class Time containing the product of arguments.

    NOTE: The method here using while-loops is not the most efficient way to do this, but I wanted to keep the function
    as basic and readable as possible, and also keep a similar structure to the examples given in the chapter. You should
    implement something like this in a real-world application:
    total_seconds = n * t_seconds
    new_t.hour = total_seconds // 3600 (integer division)
    remainder = total_seconds % 3600
    new_t.minute = remainder // 60
    new_t.second = remainder % 60
    """
    t_seconds = (t.hour * 3600) + (t.minute * 60) + t.second

    new_t = copy.copy(t)
    new_t.second = n * t_seconds

    while new_t.second >= 60:
        new_t.second -= 60
        new_t.minute += 1

    while new_t.minute >= 60:
        new_t.minute -= 60
        new_t.hour += 1

    return new_t


fin_time = Time()
fin_time.hour = 3
fin_time.minute = 15
fin_time.second = 42

def race_time(t, distance):
    """Takes a Time object that represents the finishing time in a race, the distance, and returns a Time object that
    represents the average pace.
    ARGS:
        t: instance of class Time.
        distance: race distance in miles or km.
    RETURNS:
        pace: average pace.
    """
    t_in_seconds = (t.hour * 3600) + (t.minute * 60) + t.second
    pace_per_mile = t_in_seconds / distance

    pace = Time()
    pace.hour, pace.minute, pace.second = 0, 0, 0
    pace = mul_time(pace, pace_per_mile)

    return pace



# Exercise 16-2: The datetime module provides time objects that are similar to the Time objects in this chapter, but they
# provide a rich set of methods and operators. Read the documentation at http://docs.python.org/3/library/datetime.html.
# 1. Use the datetime module to write a program that gets the current date and prints the day of the week.
# 2. Write a program that takes a birthday as input and prints the user's age and the number of days, hours, minutes and
#    seconds until their next birthday.
# 3. For two people born on different days, there is a day when one is twice as old as the other. That's their Double Day.
#    Write a program that takes two birthdays and computes their Double Day.
# 4. for a little more challenge, write the more general version that computes the day when one is n times older than
#    the other.