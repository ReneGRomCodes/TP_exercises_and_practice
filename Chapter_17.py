# Exercise 17-1: Can't solve this one. Not because it's difficult, but because the website for the necessary code is not
# available anymore. so... sorry.


# Exercise 17-2: This exercise is a cautionary tale about one of the most common, and difficult to find, errors in
# Python. Write a definition for a class named 'Kangaroo' with the following methods:
# 1. An __init__() method that initializes an attribute named 'pouch_contents' to an empty list.
# 2. A method named 'put_in_pouch()' that takes an object of any type and adds it to 'pouch_contents'.
# 3. A __str__() method that returns a string representation of the 'Kangaroo' object and the contents of the pouch.
# Test your code by creating two 'Kangaroo' objects, assigning them to variables named 'kanga' and 'roo', and then adding
# 'roo' to the contents of 'kanga's pouch.

class KangarooError:
    """Kangaroo class that leads to the error the exercise expects."""

    def __init__(self, pouch_contents=[]):      # Using a mutable object (like a list) as a default value means that
                                                # *all* instances of this class will share the *same* list. Any change
                                                # made by one instance will appear in all others, leading to confusing,
                                                # hard-to-find bugs.
        self.pouch_contents = pouch_contents


class Kangaroo:
    """Represents a kangaroo... or it's pouch?"""

    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        return f"{self.pouch_contents}"

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)
print(kanga)
