# Exercise 10-1: Write a function called 'nested_sum' that takes a list of lists of integers and adds up the elements
# from all the nested lists.

# For example:
# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))
# 21

nested_list = [[1, 2], [3], [4, 5, 6]]

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

list = [1, 2, 3]

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

list = [1, 2, 3, 4]

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

list = [1, 2, 3, 4]

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
    if t == sorted(t):
        return True
    return False


# Exercise 10-6: Write a function called 'is_anagram' that takes two strings and returns 'True' if they are anagrams.

def is_anagram(s1, s2):
    pass


# Exercise 10-7: Write a function called 'has_duplicates' that takes a list and returns 'True' if there is any element
# that appears more than once. It should not modify the original list.

def has_duplicates(t):
    pass
