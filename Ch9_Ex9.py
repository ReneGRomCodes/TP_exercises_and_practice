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
    # Remove separators and spaces from 's2' to avoid incorrect return value.
    s2 = s2.replace(",", "").replace(" ", "")

    for letter in s2:
        if letter.lower() not in s1.lower():
            continue
        else:
            return False

    return True


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


# Exercise 9-4: Write a function named 'uses_only' that takes a word and a string of letters, and that returns 'True'
# if the word contains only letters in the list.

def uses_only(s1, s2):
    """Check if string 's1' contains only letters in string 's2' and return 'False' if any letters not found in 's2' are
    used in 's1'."""
    # Remove separators and spaces from 's2' to avoid incorrect return value.
    s2 = s2.replace(",", "").replace(" ", "")

    for letter in s1:
        if letter.lower() in s2.lower():
            continue
        else:
            return False

    return True


# Exercise 9-5: Write a function named 'uses_all' that takes a word and a string of letters, and that returns 'True'
# if the word uses all the required letters at least once. How many words are there that use all the vowels 'aeiou? How
# about 'aeiouy'?

def uses_all(s1, s2):
    """Check if string 's1' contains all letters in string 's2' and return 'True' if all letters from 's2' are found in
    's1'."""
    # Remove separators and spaces from 's2' to avoid incorrect return value.
    s2 = s2.replace(",", "").replace(" ", "")

    for letter in s2:
        if letter.lower() in s1.lower():
            continue
        else:
            return False

    return True


# Check for words that use 'aeiou' and 'aeiouy'.
word_count_1 = 0
word_count_2 = 0

with open("Ch9_words.txt") as f:
    for line in f:
        if uses_all(line, "aeiou"):
            word_count_1 += 1
            if uses_all(line, "y"):
                word_count_2 += 1


print(f"There are {word_count_1} words that use 'AEIOU' and {word_count_2} that use 'AEIOUY'.")


# Exercise 9-6: Write a function called 'is_abecedarian' that returns 'True' if the letters in a word appear in
# alphabetical order (double letters are okay). How many abecedarian words are there?

def is_abecedarian(word):
    """Check string 'word' for alphabetical order of its characters. Return 'True' if alphabetical."""
    # Convert 'word' to lowercase to ensure case-insensitive comparison considering 'ord()' function.
    word = word.lower()

    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if ord(word[i]) > ord(word[j]):
                return False

    return True


# Exercise 9-7: Car Talk Puzzler (see book).

def find_word():
    """Find and print all words with three consecutive double letters in 'Ch9_words.txt'."""
    with open("Ch9_words.txt") as f:
        for line in f:
            n = 0
            while n < (len(line) - 5):
                if line[n] == line[n+1] and line[n+2] == line[n+3] and line[n+4] == line[n+5]:
                    print(line)
                n += 1


# Exercise 9-8: Car Talk Puzzler (see book).

def is_palindrome(x):
    """Check if string 'x' is palindrome."""
    if x == x[::-1]:
        return True
    else:
        return False


def odometer_palindrome_puzzle():
    """Yeah, I'm not even trying to explain what this one does... just read the "Car Talk Puzzler" in the book ;) """

    for i in range(0, 1_000_000):
        first_odo_reading = "{:06d}".format(i)
        odo_display = "{:06d}".format(i)

        if is_palindrome(odo_display[-4:]):
            odo_display = "{:06d}".format(i+1)

            if is_palindrome(odo_display[-5:]):
                odo_display = "{:06d}".format(i+2)

                if is_palindrome(odo_display[1:4]):
                    odo_display = "{:06d}".format(i+3)

                    if is_palindrome(odo_display[::]):
                        print(first_odo_reading)


# Exercise 9-9: Car Talk Puzzle (see book).

# Starting values according to the riddle.
age_son = 37
age_mother = 73
counter = 6

while counter < 8:
    age_son += 1
    age_mother += 1
    if str(age_son)[::-1] == str(age_mother):
        counter += 1

print(f"You are now {age_son} years old.")

# Actual answer is 37. It seems to be a trick question as the son mentioned his current age in the first sentence before
# asking, when he arrives home from his visit to his mother, "how old am I now?".

# Variation on the exercise letting the user input the age of the mother at birth and her current age, and print out the
# ages of both the child and the mother when the ages have matched in the past and the next time they will match.

def reverse_age_coincide():
    counter = 0
    age_child = 0
    age_mother = int(input("How old was the mother at the time of birth? "))
    age_mother_current = int(input("How old is the mother now? "))

    while age_mother <= age_mother_current:
        if str(age_child).zfill(2)[::-1] == str(age_mother):
            counter += 1

            if counter == 1:
                age_coincide = "1st"
            elif counter == 2:
                age_coincide = "2nd"
            elif counter == 3:
                age_coincide = "3rd"
            else:
                age_coincide = str(counter) + "th"

            print(f"At the {age_coincide} time the reverse ages coincided the mother was {age_mother} and the child was"
                  f" {age_child} years old.")

            age_mother += 1
            age_child += 1

        else:
            age_mother += 1
            age_child += 1

    while True:
        if str(age_child).zfill(2)[::-1] == str(age_mother):
            print(f"The next time the reverse ages coincide, the mother will be {age_mother} years old and the child "
                  f"will be {age_child} years old.")
            break
        elif age_mother == 98:
            if counter >= 1:
                print("Sorry, but no further reasonable reverse ages could be found.")
                break
            else:
                print("Sorry, but no reasonable reverse ages could be found.")
                break
        else:
            age_mother += 1
            age_child += 1


reverse_age_coincide()
