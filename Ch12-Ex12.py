# I Struggled a bit with the following exercises, so I relied heavily on the solutions from GitHub user STRZGR
# (https://github.com/STRZGR) to figure them out. His solutions are more comprehensive than the ones here, so I
# recommend checking out his repository on "Think Python": https://github.com/STRZGR/ThinkPython


# Exercise 12-1: Write a function called 'most_frequent' that takes a string and prints the letters in decreasing order
# of frequency. Find text samples from several different languages and see how letter frequency varies between
# languages.

def most_frequent(text):
    """Take a string 'text' and print the letters in decreasing order of frequency with percentage their percentage."""
    d = {}

    for s in text:
        if s.isalpha():
            s = s.lower()
            d[s] = 1 + d.get(s, 0)

    for (y, z) in reversed(sorted(zip(d.values(), d.keys()))):
        print("'{}': {:.3f}%".format(z, (y / len(text)) * 100))


# Exercise 12-2: More anagrams!
# 1. Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

def sort_letters(s):
    """Take string 's' and return new string in alphabetical order."""

    return ''.join(sorted(list(s.lower())))


def find_anagrams(file):
    """Take text from 'file' and return list of tuples of anagrams.
    First item: number of anagrams formed.
    Seconds item: letters used.
    Third item: anagrams.
    """

    sorted_dict = {}

    for line in file:
        orig_word = line.strip()
        sorted_word = sort_letters(orig_word)
        sorted_dict.setdefault(sorted_word, []).append(orig_word)

    anagrams = []

    for k, v in sorted_dict.items():
        l = len(v)
        if l > 1:
            anagrams.append((l, k, v))

    return anagrams


# 2. Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest,
#    and so on.

def find_anagrams_sorted(file):
    """
    Takes text from 'file' and return a list of tuples of anagrams in decreasing order of frequency.
    First item: number of anagrams formed.
    Seconds item: letters used.
    Third item: anagrams.
    """

    anagrams = find_anagrams(file)
    longest_list_anagrams = []

    for l, k, v in reversed(sorted(anagrams)):
        longest_list_anagrams.append((l, k, v))

    return longest_list_anagrams


# 3. In Scrabble, a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, to form an
#    eight-letter word. What collection of eight letters forms the most possible bingos'?

def find_most_scrabble_bingos(file):
    """
    Take text from 'file' and return list with tuples that form possible bingos in decreasing order of frequency of
    anagrams formed.
    First item: number of anagrams formed.
    Seconds item: letters used.
    Third item: anagrams.
    """

    sorted_anagrams_list = find_anagrams_sorted(file)

    bingos = []
    for l, k, v in sorted_anagrams_list:
        if len(k) == 8:
            bingos.append((l, k, v))

    return bingos


# Exercise 12-3: Two words form a "metathesis pair" if you can transform one into the other by swapping two letters; for
# example, "converse" and "conserve". Write a program that finds all the metathesis pairs in the dictionary.

def calculate_difference(word1, word2):
    """Calculate the number of different characters in 'word1' and 'word2'."""
    if len(word1) != len(word2):
        raise ValueError("Words must be the same length.")

    diff = 0
    for x, y in zip(word1, word2):
        if x != y:
            diff += 1

    return diff


def find_metathesis_pairs(file):
    """Take words from file 'file' and return a list of metathesis pairs 'word_pairs'."""

    # make anagrams
    anagrams = find_anagrams(file)

    word_pairs = []

    # cycle through the tuples of anagrams and pull out words which only differ by two letters.
    for length, letter, ana in anagrams:
        for i in range(len(ana)):
            for j in range(i + 1, len(ana)):
                if calculate_difference(ana[i], ana[j]) == 2:
                    word_pairs.append([ana[i], ana[j]])

    return word_pairs


# Exercise 12-4: View the book for the full "Car Talk Puzzler".
# Write a program to find all words that can be reduced this way and then the longest one.
# Suggestions:
# 1. You might want to write a function that takes a word and computes a list of all the words that can be formed by
#    removing one letter. These are the "children" of the word.
# 2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can consider the empty
#    string reducible.
# 3. The wordlist I provided, "Ch9_words.txt", doesn't contain single letter words. So you might want to add "I", "a"
#    and the empty string.
# 4. To improve the performance of your program, you might want to memoize the words that are known to be reducible.

# TODO I'll come back to this one later. Turns out to be way more complicated than I first thought.