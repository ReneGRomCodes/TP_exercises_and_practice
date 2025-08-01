# A function object is a value you can assign to a variable or pass as an argument. For example, 'do_twice' is a
# function that takes a function as an argument and calls it twice:

# def do_twice(f):
#   f()
#   f()

# Here's an example that uses 'do_twice' to call a function named 'print_spam' twice:

# def print_spam():
#   print("spam")

# do_twice(print_spam)


# 2. Modify 'do_twice' so that it takes two arguments, a function object and a value, then calls the function twice,
# passing the value as an argument.

def do_twice(f, s):
    f(s)
    f(s)


# 3. Copy the definition of 'print_twice' from earlier in this chapter into you script.

def print_twice(s):
    print(s)
    print(s)


# 4. Use the modified version of 'do_twice' to call 'print_twice' twice, passing 'spam' as an argument.

do_twice(print_twice, "spam")


# 5. Define a new function called 'do_four' that takes a function object and a value and calls the function four times,
# passing the value as a parameter. There should be only two statements in the body of this function, not four.

def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)
