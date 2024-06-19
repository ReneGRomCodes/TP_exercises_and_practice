# Exercise 9-1: Write a program that reads 'Ch9_words.txt' and print only the words with more than 20 characters (not
# counting whitespace).

def print_words_20_char():
    """Check 'Ch9_words.txt' for words with more than 20 characters and print them."""
    with open("Ch9_words.txt") as f:
        for line in f:
            word = line.strip()
            if len(word) >= 20:
                print(word)


# Exercise 9-2: Write a function called 'has_no_e' that that return 'True' if the given word doesn't have the letter 'e'
# in it.
# Modify your program from the previous section to print only the words that have no 'e' and compute the percentage of
# the words in the list that have no 'e'.

def has_no_e(s):
    """Check string 's' for occurrences of the letter 'e' and returns 'True' if absent and 'False' if not."""
    if "e" not in s.lower():
        return True
    else:
        return False


def print_no_e():
    """Check 'Ch9_words.txt' for without the letter 'e', print them and calculate the percentage of words without the
    letter 'e'."""
    with open("Ch9_words.txt") as f:
        # Declare starting values for word count variables.
        word_count = 0
        word_count_no_e = 0

        for line in f:
            word_count += 1
            word = line.strip()
            if has_no_e(word):  # Use of function 'has_no_e' check for truthiness.
                word_count_no_e += 1
                print(word)

    print(word_count)
    print(f"The percentage of words without the letter 'e' is {word_count_no_e / word_count * 100:.2f}%.")


# Exercise 9-3: Write a function named 'avoids' that takes a word and a string of letters, and that returns 'True' if
# the word doesn't use any of the forbidden letters.
# Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that
# don't contain any of them. Can you find a combination of five forbidden letters that excludes the smallest number of
# words?

def avoids(s1, s2):
    """Check if string 's1' contains any letters contained in string 's2' and return 'True' if no letter from 's2' are
    found in 's1'."""
    # Remove separators and spaces from 's2' to avoid incorrect 'True' value returned.
    s2 = s2.replace(",", "").replace(" ", "")

    flag = True
    for letter in s2:
        if letter.lower() not in s1.lower():
            continue
        else:
            return False

    return flag


def avoids_user():
    """Prompt the user for a string of 'forbidden letters' and check words 'Ch9_words.txt' for occurrence. Print the
    amount of words not containing the 'forbidden letters'."""
    forbidden_letters = input("Enter series of 'forbidden letters': ")
    # Start counter with value of 0.
    word_count = 0

    with open("Ch9_words.txt") as f:
        for line in f:
            if avoids(line, forbidden_letters):
                word_count += 1

    print(word_count)