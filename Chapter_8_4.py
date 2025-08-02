# A Caesar cypher is a weak form of encryption that involves "rotating" each letter by a fixed number of places.
# Write a function called 'rotate_word' that takes a string and an integer as parameters and returns a new string that
# contains the letters from the original string rotated by the given amount.
# You might want to use the built-in function 'ord', which converts a character to a numeric code, and 'chr' which
# converts numeric codes to characters. But beware: numeric code for uppercase letters are different.

def rotate_word(s, n):
    """Take string 's' and rotate it by 'n' number of places through the alphabet."""
    encoded_s = ""
    for letter in s:
        encoded_letter = (chr(ord(letter) + n))
        encoded_s += encoded_letter

    return encoded_s


# Alternative letting the user input a string and a value for 'n'.
def rotate_word_user():
    """Take user input 's' and rotate it by user input 'n' number of places through the alphabet."""
    s = str(input("Enter a string to encode: "))
    n = int(input("Enter a number for encryption: "))

    encoded_s = ""
    for letter in s:
        encoded_letter = (chr(ord(letter) + n))
        encoded_s += encoded_letter

    return encoded_s
