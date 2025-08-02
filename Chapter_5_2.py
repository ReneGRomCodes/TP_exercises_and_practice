# Fermat's Last Theorem says that there are no positive integers 'a', 'b' and 'c' such that
# a^n + b^n = c^n
# for any values of 'n' greater than 2.

# 1. Write a function names 'check_fermat' that takes four parameters (a, b, c and n) and checks to see if Fermat's
# Theorem holds. If 'n' is greater than two and 'a^n + b^n = c^n' the program should print "Holy smokes, Fermat was
# wrong!". Otherwise, the program should print "No, that doesn't work.".

def check_fermat(a, b, c, n):
    """Check Fermat's Last Theorem and print outcome."""
    calc = a**n + b**n
    result = c**n

    # Check for valid input.
    if a <= 0 or b <= 0 or c <= 0:
        print("a, b, and c must be positive integers.")
    elif n <= 2:
        print("n must be an integer greater than 2.")
    # Check the actual theorem.
    elif n > 2 and calc == result:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


# 2. Write a function that prompts the user to input values for 'a', 'b', 'c' and 'n', converts them to integers and
# uses 'check_fermat' to check whether they violate Fermat's Theorem.

def check_fermat_input():
    """Take user input for 'a', 'b', 'c' and 'n' and calls function 'check_fermat()'."""
    a = int(input("Enter value for 'a': "))
    b = int(input("Enter value for 'b': "))
    c = int(input("Enter value for 'c': "))
    n = int(input("Enter value for 'n': "))

    check_fermat(a, b, c, n)
