# Exercise 14-1: Write a function called 'sed' that takes a pattern string, a replacement string, and two filenames as
# arguments. It should read the first file and write its contents into the second file (creating it if necessary). If
# the pattern string appears anywhere in the file, it should be replaced with replacement string.
# If an error occurs while opening, reading or closing files, your program should catch the exception, print an error
# message and exit.

def sed(p_string, r_string, origin_file, target_file):
    """Replace occurrences of 'p_string' in 'origin_file' with 'r_string' and save new text in 'target_file'.
    ARGS:
        p_string: pattern string to be replaced with 'r_string'.
        r_string: replacement string to replace occurrences of 'p_string'.
        origin_file: path to the file to process.
        target_file: path to the file to save processed text.
    """
    try:
        fin = open(origin_file, "r")
        fout = open(target_file, "w")

        fin_contents = fin.read().replace(p_string, r_string)
        fout.write(fin_contents)

        fin.close()
        fout.close()

    except:
        print("Error! Exiting program.")


def sed_alternative(p_string, r_string, origin_file, target_file):
    """Alternative solution using 'with open' command and more detailed error handling.
    ARGS:
        p_string: pattern string to be replaced with 'r_string'.
        r_string: replacement string to replace occurrences of 'p_string'.
        origin_file: path to the file to process.
        target_file: path to the file to save processed text.
    """
    try:
        with open(origin_file, "r") as fin, open(target_file, "w") as fout:
            fin_contents = fin.read().replace(p_string, r_string)
            fout.write(fin_contents)

    except FileNotFoundError:
        print(f"File '{origin_file}' not found! Exiting program.")
    except PermissionError:
        print(f"You don't have permission to access file! Exiting program.")
    except OSError:
        print("Error! Exiting program.")


# Exercise 14-2: Use the solution from exercise 12-2 to create a dictionary that maps from sorted string of letters to
# a list of words containing anagrams.
# Write a module that provides two new functions: 'store_anagrams()' to store the anagram dictionary in a "shelf", and
# 'read_anagrams()' to look up a words and return a list of its anagrams.
"""NOTE: The book asks you to download the solution from 'http://thinkpython2.com/code/anagram_sets.py', but at the time
of my writing this, the site seems to be down."""
import shelve


def sort_letters(s):
    """Take string 's' and return new string in alphabetical order."""
    return ''.join(sorted(list(s.lower())))


def find_anagrams(file):
    """Take text from 'file' and return dict of anagrams.
    ARGS:
        file: path to the file to process.
    RETURNS:
        anagrams_dict
    """
    anagrams_dict = dict()

    with open(file, "r") as f:
        text = f.read()
        words_set = set(text.split())

        for word in words_set:
            sorted_word = sort_letters(word)
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = {word}
            else:
                anagrams_dict[sorted_word].add(word)

    return anagrams_dict


def store_anagram(text, file):
    """Create and store anagrams dictionary from text into a shelf file.
    Args:
        text: path to the text file to process.
        file: path for the shelf file to store anagrams.
    """
    anagrams_dict = find_anagrams(text)

    with shelve.open(file) as shelf:
        for k, v in anagrams_dict.items():
            shelf[k] = v


def read_anagrams(word, file):
    """Retrieve a list of anagrams for a given word from a shelf file.
    ARGS:
        word: Word to find anagrams for.
        file: Path to the shelf file to read from.
    RETURNS:
        list: List of anagrams for the word.
    """
    sorted_word = sort_letters(word)

    with shelve.open(file, "r") as shelf:
        return list(shelf[sorted_word])



# Exercise 14-3: In a large collection of MP3 files, there may be more than one copy of the same song, stored in different
# directories or with different filenames. The goal of this exercise is to search for duplicates.
# 1. Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete
#    paths for all files with a given suffix (like .mp3). Hint: 'os.path' provides several useful functions for manipulating
#    file- and path names.
# 2. To recognize duplicates, you can use 'md5sum' to compute a checksum for each file.
# 3. To double-check, you can use the Unix command 'diff'.
