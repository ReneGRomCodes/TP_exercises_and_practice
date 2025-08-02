# Exercise 11-1: Write a function that reads words in 'Chapter_9_words.txt' and stores them as keys in a dictionary. It
# doesn't matter what the values are. Then you use the in operator as a fast way to check whether a string is in the
# dictionary.

words = "Chapter_9_words.txt"


def build_words_dict(file):
    """Build a dictionary from txt file 'file', return the lines as keys and the length of the lines as values."""
    words_dict = dict()

    with open(file) as f:
        for line in f:
            words_dict[line[:-1]] = len(line) - 1  # [:-1] and -1 to remove the '\n' at the end of each line in file.

    return words_dict


def find_word(s, file):
    """Search for string 's' (case-insensitive) in dictionary build from txt file 'file' and output message."""
    search_words_dict = build_words_dict(file)

    if s.lower() in search_words_dict:
        print(f"The word '{s.upper()}' is in the dictionary with the assigned value {search_words_dict[s]}.")
    else:
        print(f"The word '{s.upper()}' is not in the dictionary.")


# Exercise 11-2: Read the documentation of the dictionary method 'setdefault' and use it to write a more concise version
# of 'invert_dict'.

def invert_dict(d):
    """Take dictionary 'd' and return new dictionary 'inverse', where 'd's key-value-pairs are inverted."""
    inverse = dict()

    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)

    return inverse


# Exercise 11-3: Memoize the Ackermann function from exercise 6-2 and see if memoization makes it possible to evaluate
# the function with bigger arguments than 'm=3, n=4'.

# Function copied from exercise 6-2:
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


known = {}


def ack_memo(m, n):
    if m in known:
        return known[m]
    if n in known:
        return known[m]

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))



# Exercise 11-4: If you did exercise 10-7, you already have a function named 'has_duplicates' that takes a list as a
# parameter and returns 'True' if there is any object that appears more than once in the list. Use a dictionary to write
# a faster, simpler version of 'has_duplicates'.

def has_duplicates_dict(t):
    """Take list 't' and check for duplicate items (case-sensitive). Return 'True' if multiple items are found, 'False'
    if not."""
    t_dict = dict()

    for item in t:
        if item in t_dict:
            return True
        else:
            t_dict[item] = 1

    return False
