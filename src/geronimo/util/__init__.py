"""
Small utility functions.
"""

from functools import lru_cache


@lru_cache
def fibonacci(n: int) -> int:
    """
    Returns the nth number in the Fibonacci series, starting to count at zero.
    Only works for the positive Fibonacci series. Uses caching to be more
    efficient.

    So fib(0) = 1, fib(1) = 1, fib(2) = 2, fib(3) = 3, fib(4) = 5, ...
    """

    if n < 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


fib = fibonacci


@lru_cache
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Uses the iterative modern Euclidean algorithm to quickly find the greatest
    common divisor for two integers, a and b.
    """

    while b != 0:
        c = a % b
        a, b = b, c

    return a


gcd = greatest_common_divisor
