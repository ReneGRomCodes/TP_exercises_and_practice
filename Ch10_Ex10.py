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
