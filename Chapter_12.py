# Exercise 12-1: Write a function called 'most_frequent' that takes a string and prints the letters in decreasing order
# of frequency. Find text samples from several different languages and see how letter frequency varies between
# languages.


def most_frequent(text):
    """Take a string 'text' and print the letters in decreasing order of frequency with their percentage.
    ARGS:
        text: string to be processed.
    """
    histogram = {}

    for s in text:
        s = s.lower()
        alpha = s.isalpha()

        if alpha and s not in histogram:
            histogram[s] = 1
        elif s in histogram:
            histogram[s] += 1

    s_sum = sum(histogram.values())
    sorted_frequency = reversed(sorted(zip(histogram.values(), histogram.keys())))

    for letter, value in sorted_frequency:
        print(f"{letter}: {(value / s_sum) * 100:.2f}%")


# Exercise 12-2: More anagrams!
# 1. Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

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


# 2. Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest,
#    and so on.

def find_anagrams_sorted(file):
    """Takes text from 'file' and return a list of tuples of anagrams in decreasing order of frequency.
    ARGS:
        file: path to file to process.
    RETURNS:
        list(number of anagrams formed, letters used, anagrams)
    """
    anagrams = find_anagrams(file)
    longest_list_anagrams = []

    for l, k, v in reversed(sorted(anagrams)):
        longest_list_anagrams.append((l, k, v))

    return longest_list_anagrams


# 3. In Scrabble, a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, to form an
#    eight-letter word. What collection of eight letters forms the most possible bingos'?

def find_most_scrabble_bingos(file):
    """Take text from 'file' and return list with tuples that form possible bingos in decreasing order of frequency of
    anagrams formed.
    ARGS:
        file: path to file to process.
    RETURNS:
        list(number of anagrams formed, letters used, anagrams)
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
    """Calculate the number of different characters in 'word1' and 'word2'.
    ARGS:
        word1: strings to check for differences.
        word2: strings to check for differences.
    RETURNS:
        number of different characters.
    """
    if len(word1) != len(word2):
        raise ValueError("Words must be the same length.")

    diff = 0
    for x, y in zip(word1, word2):
        if x != y:
            diff += 1

    return diff


def find_metathesis_pairs(file):
    """Take words from file 'file' and return a list of metathesis pairs 'word_pairs'.
    ARGS:
        file: path to file to process.
    RETURNS:
        list of metathesis pairs.
    """
    anagrams = find_anagrams(file)
    word_pairs = []

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
# 3. The wordlist I provided, "Chapter_9_words.txt", doesn't contain single letter words. So you might want to add "I",
#    "a" and the empty string.
# 4. To improve the performance of your program, you might want to memoize the words that are known to be reducible.

# TODO I'll come back to this one later. Turns out to be way more complicated than I first thought.