# The built-in function 'eval' takes a string and evaluates it using the Python interpreter.
# Write a function called 'eval_loop' that iteratively prompts the user, takes the resulting input and evaluates it
# using 'eval', then prints the result.
# It should continue until the user enters "done" and then return the value of the last expression it evaluated.

def eval_loop():
    """Evaluate user input and print it until input = 'done'. Then exit and return last evaluated value."""

    # Starting value for 'output' if no input is given by user during first iteration.
    output = None

    while True:
        user_input = input("Input string to evaluate or enter 'done' to exit: ")
        if user_input.lower() == "done":
            break
        output = eval(user_input)
        print(output)

    return output


print(eval_loop())
