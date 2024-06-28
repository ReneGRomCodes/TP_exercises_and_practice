# Exercise 11-1: Write a function that reads words in 'Ch9_words.txt' and stores them as keys in a dictionary. It
# doesn't matter what the values are. Then you use the in operator as a fast way to check whether a string is in the
# dictionary.

words = "Ch9_words.txt"


def build_words_dict(t):
    """Build a dictionary from txt file 't', return the lines as keys and the length of the lines as values."""
    words_dict = dict()

    with open(t) as f:
        for line in f:
            words_dict[line[:-1]] = len(line) - 1  # [:-1] and -1 to remove the '\n' at the end of each line in file.

    return words_dict


def find_word(s, t):
    """Search for string 's' (case-insensitive) in dictionary build from txt file 't' and output message."""
    search_words_dict = build_words_dict(t)

    if s.lower() in search_words_dict:
        print(f"The word '{s.upper()}' is in the dictionary with the assigned value {search_words_dict[s]}.")
    else:
        print(f"The word '{s.upper()}' is not in the dictionary.")


# Exercise 11-2: Read the documentation of the dictionary method 'setdefault' and use it to write a more concise version
# of 'invert_dict'.


# Exercise 11-3: Memoize the Ackermann function from exercise 6-2 and see if memoization makes it possible to evaluate
# the function with bigger arguments.


# Exercise 11-4: If you did exercise 10-7, you already have a function named 'has_duplicates' that takes a list as a
# parameter and returns 'True' if there is any object that appears more than once in the list. Use a dictionary to write
# a faster, simpler version of 'has_duplicates'.


# Exercise 11-5: Two words are "rotate pairs" if you can rotate one of them and get the other. Write a program that
# reads a wordlist and finds all the rotate pairs.
