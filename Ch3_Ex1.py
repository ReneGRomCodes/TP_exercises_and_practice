# Write a function named 'right_justify' that takes a string named 's' as a parameter and prints the string with enough
# leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    """Take string 's' and add leading spaces to get an output string with an overall length of 70."""
    if len(s) > 70:
        print("The string has too many characters!")
    else:
        leading_space = " " * (70 - len(s))
        print(leading_space + s)

right_justify("Monty")


# Alternative solution using string formatting.

def right_justify_alt(s):
    """Take string 's' and add leading spaces to get an output string with an overall length of 70."""
    if len(s) > 70:
        print("The string has too many characters!")
    else:
        s = f"{s:>70}"
        print(s)

right_justify_alt("Monty")
