# Exercise 13-1: Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from
# the words and converts them to lowercase.
import string


def get_words(text, encode="utf8"):
    """Return a list of words from file 'text'. Default text encoding is "utf8"."""
    punct = string.punctuation

    out = " " * len(punct)

    opened_text = open(text, 'r', encoding=encode)
    t = []
    for line in opened_text:
        translation = line.maketrans(punct, out)
        for word in line.translate(translation).split():
            t.append(word.strip().lower())

    return t


# Exercise 13-2: Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-copyright book in
# plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip over the header information at
# the beginning of the file and process the rest of the words as before.
# Then modify the program to count the total number of words in the book and the number of times each word is used.
# Print the number of different words used in the book. Compare different books by different authors, written in
# different eras. Which author uses the most extensive vocabulary?

def get_words_2(text, encode="utf8"):
    """Return a list of words from file 'text'. Default text encoding is "utf8". Adjusted to work with text files from
    "Project Gutenberg"."""

    stripped = string.punctuation

    stripped += string.whitespace

    opened_text = open(text, 'r', encoding=encode)
    t = []
    flag = False
    start = "*** START OF"
    end = "*** END OF"

    for line in opened_text:

        # start reading in lines after boilerplate
        if start in line and flag == False:
            flag = True

        # return word list once boilerplate has been reached
        elif end in line and flag == True:
            return t
        else:
            pass

    return t


def count_words(text_list):
    """Take list 'text_list' and return a tally in dictionary 'tally_words'."""
    tally_words = {}

    for word in text_list:
        tally_words[word] = 1 + tally_words.get(word, 0)

    return tally_words


# Exercise 13-3: Modify the program from the previous exercise to print the 20 most frequently used words in the book.

def n_most_common_words(text, encode="utf8"):
    """Return a list of the 20 most common words in a "Project Gutenberg" text."""

    words = get_words_2(text, encode)
    tally = count_words(words)

    sorted_words = []

    for (y, z) in reversed(sorted(zip(tally.values(), tally.keys()))):
        sorted_words.append([z, y])

    return sorted_words[:20]


"""
# NOTE: I took a break here for about two years. So if my overall style changed a bit it's because I am not completely
# useless anymore when it comes to coding... just mostly useless ;) I will try to come up with solutions that are as
# close as possible to what the book would expect you to do. The alternative solutions provided will probably be a bit
# better than the ones I did previously... at least I hope. Would be embarrassing if I learned jack-shit over the past
# years. Anyway, enjoy!
# --- René
"""


# Exercise 13-4: Modify the previous program to read a word list (use 'Chapter_9_words.txt') and then print all the words
# in the book that are not in the word list. How many of them are typos? How many of them are common words that should be
# in the word list and how many of them are really obscure?

def check_book_words(word_list, book):
    """Check for and print out words from 'book' that don't appear in list 'word_list'.
    NOTE: this is a very basic version that does not clean the output from things like contractions, numbers or symbols
    to keep the basic logic clear.
    ARGS:
        word_list: txt file containing words for checks.
        book: txt file containing a book.
    """
    check_words = get_words(word_list)
    book_words = get_words(book)
    word_dict = {}

    for word in book_words:
        if word not in check_words:
            word_dict[word] = None

    for key in word_dict.keys():
        print(key)


# Alternative solution using sets for improved performance.
def check_book_words_alternative(word_list, book):
    """Check for and print out words from 'book' that don't appear in list 'word_list'.
    NOTE: this is a very basic version that does not clean the output from things like contractions, numbers or symbols
    to keep the basic logic clear.
    ARGS:
        word_list: txt file containing words for checks.
        book: txt file containing a book.
    """
    check_words = set(get_words(word_list))
    book_words = set(get_words(book))

    word_set = book_words - check_words

    for word in word_set:
        print(word)
