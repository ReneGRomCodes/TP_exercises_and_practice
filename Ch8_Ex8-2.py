# There is a string method called 'count' that is similar to the function in "Looping and Counting" on page 89 (see
# book). Read the documentation of this method and write an invocation that counts the number of a's in 'banana'.

# function from page 89 for reference:
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)


# Solution using the 'count' method.
fruit = "banana"
print(fruit.count("a"))
