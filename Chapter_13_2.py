import string


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
