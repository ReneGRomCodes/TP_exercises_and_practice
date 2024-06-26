# The following functions are all intended to check whether a string contains any lowercase letters, but at least some
# of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a
# string).


# Only tests the first character and immediately returns 'True' or 'False'.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# Ignores the parameter and only checks if "c" in the 'ifs-statement' is lowercase, therefor always returns 'True'.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False


# Only tests the first character and immediately returns 'True' or 'False'.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag


# Works as intended because it checks every character in 's' and only changes 'flag' if a lowercase letter is found
# before returning 'flag'
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# Only returns 'True' if all characters in 's' are lowercase. Returns 'False' as soon as one uppercase character is
# found.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
