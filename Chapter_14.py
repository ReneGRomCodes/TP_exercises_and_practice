# Exercise 14-1: Write a function called 'sed' that takes a pattern string, a replacement string, and two filenames as
# arguments. It should read the first file and write its contents into the second file (creating it if necessary). If
# the pattern string appears anywhere in the file, it should be replaced with replacement string.
# If an error occurs while opening, reading or closing files, your program should catch the exception, print an error
# message and exit.

def sed(p_string, r_string, origin_file, target_file):
    """Replace occurrences of 'p_string' in 'origin_file' with 'r_string' and save new text in 'target_file'.
    ARGS:
        p_string:
        r_string:
        origin_file:
        target_file:
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
# read anagrams to look up a words and return a list of its anagrams.
"""NOTE: The book asks you to download the solution from 'http://thinkpython2.com/code/anagram_sets.py', but at the time
of my writing this, the site seems to be down."""


# Exercise 14-3: In a large collection of MP3 files, there may be more than one copy of the same song, stored in different
# directories or with different filenames. The goal of this exercise is to search for duplicates.
# 1. Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete
#    paths for all files with a given suffix (like .mp3). Hint: 'os.path' provides several useful functions for manipulating
#    file- and path names.
# 2. To recognize duplicates, you can use 'md5sum' to compute a checksum for each file.
# 3. To double-check, you can use the Unix command 'diff'.
