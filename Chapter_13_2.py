import string
import random


# Exercise 13-8: Markov Analysis.

# 1. Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps
# from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to
# you to make an appropriate choice. You can test your program with prefix length 2, but you should write the program in
# a way that makes it easy to try other lengths.

def get_words(text, encode="utf8"):
    """Return a list of words from file 'text'. Default text encoding is "utf8". Adjusted to work with text files from
    "Project Gutenberg"."""
    punct = string.punctuation
    out = " " * len(punct)
    flag = False
    start = "*** START OF"
    end = "*** END OF"

    t = []

    with open(text, 'r', encoding=encode) as opened_text:
        for line in opened_text:
            # Start reading in lines after boilerplate.
            if start in line and not flag:
                flag = True

            # Break loop after boilerplate.
            elif end in line and flag:
                break

            # Add word to list when flag is 'True'.
            elif flag:
                translation = line.maketrans(punct, out)
                for word in line.translate(translation).split():
                    t.append(word.strip().lower())

    return t


def markov_analysis(text, depth):
    """Return a dictionary mapping prefixes to lists of possible suffixes from a given text file.
    ARGS:
        text: Path to the text file to analyze.
        depth: Integer representing number of words to use as the prefix.
    RETURNS:
        Dictionary where each key is a prefix (string of 'depth' words), and each value is a list of suffix words that
        follow that prefix.
    """
    prefix_suffix_dict = {}
    word_list = get_words(text)

    for index, word in enumerate(word_list):
        # Break loop when prefix has no suffix at the end of the list to avoid index error.
        if index == len(word_list) - depth:
            break

        else:
            prefix = ' '.join(word_list[index:index+depth])

            if prefix not in prefix_suffix_dict:
                prefix_suffix_dict[prefix] = []

            prefix_suffix_dict[prefix].append(word_list[index+depth])

    return prefix_suffix_dict


# Alternative using dicts of suffix frequencies.
def markov_analysis_alternative(text, depth):
    """Return a dictionary mapping prefixes to dicts of suffix frequencies from a given text file.
    ARGS:
        text: Path to the text file to analyze.
        depth: Integer representing number of words to use as the prefix.
    RETURNS:
        Dictionary where each key is a prefix (string of 'depth' words), and each value is a dict of suffix frequencies
        that follow that prefix.
    """
    prefix_suffix_dict = {}
    word_list = get_words(text)

    for index, word in enumerate(word_list):
        # Break loop when prefix has no suffix at the end of the list to avoid index error.
        if index == len(word_list) - depth:
            break

        else:
            prefix = ' '.join(word_list[index:index + depth])
            suffix = word_list[index + depth]

            if prefix not in prefix_suffix_dict:
                prefix_suffix_dict[prefix] = {}

            if suffix not in prefix_suffix_dict[prefix]:
                prefix_suffix_dict[prefix][suffix] = 1
            else:
                prefix_suffix_dict[prefix][suffix] += 1

    return prefix_suffix_dict


# 2. Add a function to the previous program to generate random text based on the Markov analysis.

def generate_text(text, word_count=100, depth=6):
    """Generate random text based on markov analysis of text file.
    ARGS:
        text: Path to the text file to analyze.
        word_count: Number of words for output text. Default is 100.
        depth: Integer representing number of words to use as the prefix. Default is 6.
    RETURNS:
        text_output: randomly generated string.
    """
    prefix_suffix_dict = markov_analysis(text, depth)
    prefix = ""
    suffix = ""
    text_output = ""

    for _ in range(word_count):
        # Build first text snippet for 'text_output'.
        if not text_output:
            prefix = random.choice(list(prefix_suffix_dict.keys()))
            suffix = random.choice(prefix_suffix_dict[prefix])
            text_output += f"{prefix} {suffix} "
        # Build further string additions for 'text_output' by creating a new prefix based on previous suffix.
        else:
            prefix = f"{' '.join(prefix.split()[1:])} {suffix}"
            suffix = random.choice(prefix_suffix_dict[prefix])
            text_output += f"{suffix} "

    return text_output


# 3. Once your program is working, you might want to try a mash-up: if you combine text from two or more books, the
# random text you generate will blend the vocabulary and phrases from the sources in interesting ways.

# List with texts from 'txt files/' for testing following functions.
TEXT_LIST = ("txt files/dracula.txt", "txt files/sherlock_holmes.txt",
             "txt files/the_moonstone.txt", "txt files/wizard_of_oz.txt")

def markov_analysis_multi(prefix_suffix_dict, text, depth):
    """Slightly modified version of function 'markov_analysis()' to allow for function 'generate_text_multi()' to handle
    multiple texts.
    ARGS:
        prefix_suffix_dict: Dictionary where each key is a prefix (string of 'depth' words), and each value is a list of
            suffix words that follow that prefix.
        text: Path to the text file to analyze.
        depth: Integer representing number of words to use as the prefix.
    RETURNS:
        prefix_suffix_dict
    """
    word_list = get_words(text)

    for index, word in enumerate(word_list):
        if index == len(word_list) - depth:
            break
        else:
            prefix = ' '.join(word_list[index:index+depth])
            if prefix not in prefix_suffix_dict:
                prefix_suffix_dict[prefix] = []
            prefix_suffix_dict[prefix].append(word_list[index+depth])

    return prefix_suffix_dict


def generate_text_multi(texts, word_count=100, depth=6):
    """Generate random text based on markov analysis of text file.
    ARGS:
        texts: list or tuple of text files to analyze.
        word_count: Number of words for output text. Default is 100.
        depth: Integer representing number of words to use as the prefix. Default is 6.
    RETURNS:
        text_output: randomly generated string.
    """
    prefix_suffix_dict = {}
    prefix = ""
    suffix = ""
    text_output = ""

    # Populate 'prefix_suffix_dict' using modified markov analysis function.
    for text in texts:
        prefix_suffix_dict = markov_analysis_multi(prefix_suffix_dict, text, depth)

    for _ in range(word_count):
        # Build first text snippet for 'text_output'.
        if not text_output:
            prefix = random.choice(list(prefix_suffix_dict.keys()))
            suffix = random.choice(prefix_suffix_dict[prefix])
            text_output += f"{prefix} {suffix} "
        # Build further string additions for 'text_output' by creating a new prefix based on previous suffix.
        else:
            prefix = f"{' '.join(prefix.split()[1:])} {suffix}"
            suffix = random.choice(prefix_suffix_dict[prefix])
            text_output += f"{suffix} "

    return text_output
