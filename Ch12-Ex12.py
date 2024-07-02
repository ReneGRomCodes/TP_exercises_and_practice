# Exercise 12-1: Write a function called 'most_frequent' that takes a string and prints the letters in decreasing order
# of frequency. Find text samples from several different languages and see how letter frequency varies between
# languages.

def most_frequent(text):
    """Take a string 'text' and print the letters in decreasing order of frequency."""
    d = {}

    for s in text:
        if s.isalpha():
            s = s.lower()
            d[s] = 1 + d.get(s, 0)

    for (y, z) in reversed(sorted(zip(d.values(), d.keys()))):
        print("'{}': {:.3f}%".format(z, (y / len(text)) * 100))


# Exercise 12-2: More anagrams!
# 1. Write a program that reads a word list from a file and prints all the sets of words that are anagrams.
# 2. Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest,
#    and so on.
# 3. In Scrabble, a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, to form an
#    eight-letter word. What collection of eight letters forms the most possible bingos'


# Exercise 12-3: Two words form a "metathesis pair" if you can transform one into the other by swapping two letters; for
# example, "converse" and "conserve". Write a program that finds all the metathesis pairs in the dictionary.

def find_metathesis_pair(file):
    pass


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
