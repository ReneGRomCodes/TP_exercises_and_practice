# Exercise 19-1: The following is a function that computes the binominal coefficient recursively:
from speechd_config import dont_ask


def binominal_coeff(n, k):
    """Compute the binominal coefficient 'n choose k'.
    ARGS:
        n: number of trials.
        k: number of successes.
    RETURNS:
        int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0

    res = binominal_coeff(n-1, k) + binominal_coeff(n-1, k-1)
    return res

# Rewrite the body of the function using nested conditional expressions.

def binominal_coeff_nested(n, k):
    """Compute the binominal coefficient 'n choose k'.
    ARGS:
        n: number of trials.
        k: number of successes.
    RETURNS:
        int
    """
    return 1 if k == 0 else 0 if n == 0 else binominal_coeff(n-1, k) + binominal_coeff(n-1, k-1)
