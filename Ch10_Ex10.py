# Exercise 10-1: Write a function called 'nested_sum' that takes a list of lists of integers and adds up the elements
# from all the nested lists.

# For example:
# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))
# 21

def nested_sum(t):
    """Take a list of lists of integers 't' and adds up the elements from all the nested lists."""
    final_sum = 0
    index = 0

    for i in range(len(t)):
        final_sum += sum(t[index])
        index += 1

    return final_sum


# Exercise 10-2: Write a function called 'cumsum' that takes a list of numbers and returns the cumulative sum; that is,
# a new list where i-th element is the sum of first i+1 elements from the original list.

# For example:
# t = [1, 2, 3]
# print(cumsum(t))
# [1, 3, 6]

def cumsum(t):
    """Take a list of numbers 't' return new list with each item being the cumulative sum of the previous items from
    't'."""
    index = 0
    cumsum_list = []

    for i in range(len(t)):
        if index == 0:
            sum = t[index]
            cumsum_list.append(sum)
            index += 1
        else:
            sum = t[index] + cumsum_list[index-1]
            cumsum_list.append(sum)
            index += 1

    return cumsum_list


# Exercise 10-3: Write a function called 'middle' that takes a list and returns a new list that contains all but the
# first and last elements.

# For example:
# t = [1, 2, 3, 4]
# middle(t)
# [2, 3]

def middle(t):
    """Take list 't', remove first and last element and return new list 'new_list'."""
    new_list = list[1:-1]
    return new_list


# Exercise 10-4: Write a function called 'chop' that takes a list, modifies it by removing the first and last elements,
# and returns 'None'.

# For example:
# t = [1, 2, 3, 4]
# chop(t)
# print(t)
# [2, 3]

def chop(t):
    """Take list 't' and remove first and last element."""
    del t[0], t[-1]


# Exercise 10-5: Write a function called 'is_sorted' that takes a list as a parameter and return 'True' if the list is
# sorted in ascending order and 'False' otherwise.

# For example:
# print(is_sorted([1, 2, 2]))
# True
# print(is_sorted(['b', 'a']))
# False

def is_sorted(t):
    """Check if list 't' is sorted in ascending order and return 'True' if so, 'False' if not."""
    return t == sorted(t)


# Exercise 10-6: Write a function called 'is_anagram' that takes two strings and returns 'True' if they are anagrams.

def is_anagram(s1, s2):
    """Take strings 's1' and 's2' and return 'True' if they are anagrams (not case-sensitive), 'False' if not."""
    return sorted(list(s1.lower())) == sorted(list(s2.lower()))


# Exercise 10-7: Write a function called 'has_duplicates' that takes a list and returns 'True' if there is any element
# that appears more than once. It should not modify the original list.

def has_duplicates(t):
    """Take a list 't' and return 'True' if any element appear more than once."""
    t2 = sorted(t)
    index = 0

    for i in range(len(t2)):
        if t2[index] == t2[index-1]:
            return True
        else:
            index += 1

    return False


# Expanded solution that works for lists of either numbers or strings, is case-insensitive and prints output message,
# listing the items that are found multiple times.

def has_duplicates_expanded(t):
    """Take a list 't', check for any multiple occurrences of items (case_insensitive) and prints formatted output
    message"""
    t2 = sorted(t)
    index = 0

    multi_item = []

    for i in range(len(t2)):
        if t2[index].lower() == t2[index - 1].lower():

            # Make sure that items that are found to be multiples appear only once in 'multi_item' list.
            if str(t2[index]) in multi_item:
                index += 1
                continue
            # Add item found to be multiple as type(string) for easier use when formatting final output message.
            multi_item.append(str(t2[index]).upper())
            index += 1
        else:
            index += 1

    # Build and print final output message.
    if multi_item:
        if len(multi_item) == 1:
            multi_item_s = multi_item[0]
            print(f"The item '{multi_item_s}' appears multiple times.")
        else:
            multi_item_last = multi_item.pop()
            multi_item_s = ", ".join(multi_item)
            print(f"The items '{multi_item_s}' and '{multi_item_last}' appear multiple times.")
    else:
        print("Every item appears only once.")


# Exercise 10-8: This exercise pertains to the so-called 'Birthday Paradox'. If there are 23 students in your class,
# what are the chances that two of you have the same birthday? You can estimate this probability by generating random
# samples of 23 birthdays and checking for matches.

group_size = 23


def birthday_paradox_exp(n):
    """Take group size 'n' and print approximate probability in % of two people in the group share the same birthday,
    using simple exponentiation."""
    exp = (n * (n-1)) / 2
    probability = (1 - (364/365)**exp) * 100
    message = (f"The probability that two people within a group of {n} share the same birthday is approximately "
               f"{probability:.2f}%.")
    print(message)


# Exercise 10-9: Write a function that reads the words.txt file from chapter 9 (CH9_words.txt) and build a list with one
# element per word. Write two versions of the function, one using the 'append' method and other using the idiom
# 't=t+[x]'. Which one takes longer to run and why?

word_file = "Ch9_words.txt"


# Using Append method.
def build_word_list_1(file):
    """Take text file 'file' and add every line as item into and return list 'word_list_1'."""
    word_list_1 = []
    with open(file) as f:
        for line in f:
            word_list_1.append(line.strip())

    return word_list_1


# Using the idiom 't=t+[x]'.
def build_word_list_2(file):
    word_list_2 = []
    with open(file) as f:
        for line in f:
            word_list_2 += [line.strip()]

    return word_list_2


# Answer: using the '.append' method is faster because concatenation creates a new list for each item, while '.append'
# simply adds a new item to the already existing list.


# Exercise 10-10: To check whether a word is in the word list, you could use the 'in' operator, but it would be slow,
# because it searches through the words in order. Because the words are in order, we can speed things up with a
# bisection search (aka 'binary search').
# Write a function called 'in_bisect' that takes a sorted list and a target value and returns the index of the value in
# the list if it's there, or 'False' if it's not.

# Making use of the variable 'word_file' and the function 'build_word_list_1()' as defined in the previous exercise.

word_list = build_word_list_1(word_file)


def binary_search(word, t):
    """Search for string 'word' in list 't' using binary search. Return 'True' if word is found, 'False if not."""
    # Check if list is empty.
    if len(t) == 0:
        return False

    t_bisect = len(t) // 2

    if t[t_bisect] == word:
        return True
    elif word < t[t_bisect]:
        return binary_search(word, t[:t_bisect])
    else:
        return binary_search(word, t[t_bisect + 1:])


# Exercise 10-11: Two words are a "reverse pair" if each is the reverse of the other. Write a program that finds all the
# reverse pairs in the word list.

# Making use of the list 'word_list' and the function 'binary_search()' as defined in the previous exercise.

def find_reverse_pair(t):
    """Search through list 't' for "reverse pairs" and print them."""

    # Declaring an index value mainly for the use in the function call of 'binary_search()', letting the function start
    # the search from the index of the last item checked, of instead searching through the list from the start every
    # time. Therefor speeding up the process, especially towards the end.
    index = 0

    while index < len(t):
        for item in t:
            reverse_item = item[::-1]
            if binary_search(reverse_item, t[index:]):
                if item <= reverse_item:
                    print(item, reverse_item)
            index += 1


# Expanded solution giving out constant status output on number of words searched and number of reverse pairs found,
# before printing a final output with the overall number of reverse pairs, how many of those are palindromes (as special
# cases of reverse pairs) and returns a list with each pair as item in "item - reverse_item" format.
# It is a bit clunky with the constant status output (I decided against clearing the screen every time) and hilariously
# slow, but I wanted to experiment a bit with it... so don't look at me like that ;)
def find_reverse_pair_expanded(t):
    pair_list = []
    word_counter = 0
    pair_counter = 0
    palindrome_counter = 0
    index = 0

    while index < len(t):
        for item in t:
            word_counter += 1
            reverse_item = item[::-1]

            if binary_search(reverse_item, t[index:]):
                if item <= reverse_item:
                    pair = item + " - " + reverse_item
                    pair_list.append(pair)
                    pair_counter += 1
                    if item == reverse_item:
                        palindrome_counter += 1

            print(f"Words searched: {word_counter}")
            print(f"Reverse pairs found: {pair_counter}\n")

            index += 1

    print(f"Out of {word_counter}, a total of {pair_counter} reverse pairs have been found, {palindrome_counter} of "
          f"them are palindromes.")
    return pair_list


# Exercise 10-12 Two words "interlock" if taking alternating letters from each form a new word. For example, 'shoe" and
# 'cold' interlock to form 'schooled'.
# 1. Write a program that find all pairs of words that interlock.
# 2. Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the
#    first, second or third?

# Making use of the list 'word_list' and the function 'binary_search()' as defined in the exercise 10-10.

def search_interlocking_words(t):
    """Find interlocked words in list 't', then add them to and return new list 'interlocking_words'."""
    interlocking_words = []

    for word in t:
        word_1 = word[0::2]
        word_2 = word[1::2]
        if binary_search(word_1, t) and binary_search(word_2, t):
            interlocking_words.append([word_1, word_2, word])

    # Following line added out of curiosity how many interlocking word pairs would be found (it's 1254 btw.).
    # print(len(interlocking_words))
    return interlocking_words


def search_three_interlocking_words(t):
    """Find interlocked words that can be constructed from three words in list 't', then add them to and return new list
    'three_interlocking_words'."""
    three_interlocking_words = []

    for word in t:
        word_1 = word[0::2]
        word_2 = word[1::2]
        word_3 = word[2::2]
        if binary_search(word_1, t) and binary_search(word_2, t) and binary_search(word_3, t):
            three_interlocking_words.append([word_1, word_2, word_3, word])

    # Following line added out of curiosity how many interlocking word triplets would be found (it's 560 btw.).
    # print(len(three_interlocking_words))
    return three_interlocking_words
