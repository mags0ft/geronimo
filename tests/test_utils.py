"""
Tests the utilities included in geronimo.
"""

import time
from geronimo.util import fibonacci, fib, greatest_common_divisor


CORRECT_FIB_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci() -> None:
    """
    Tests the built-in fibonacci series utility.
    """

    for n, correct in enumerate(CORRECT_FIB_NUMBERS):
        assert fibonacci(n) == correct


def test_fibonacci_speed() -> None:
    """
    Tests if the speed of the fibonacci utility is sufficient. Should be the
    case, at least if caching is used.
    """

    start: float = time.time()
    fibonacci(40)
    end: float = time.time()

    assert (end - start) < 1.0  # no longer than one second (more than enough)


def test_shorthand_fib() -> None:
    """
    Tests the shorthand function handle for the Fibonacci series.
    """

    assert fib(5) == 8


def test_greatest_common_divisor() -> None:
    """
    Tests the utility function for finding the greatest common divisor of two
    numbers, a and b.
    """

    assert greatest_common_divisor(16, 20) == 4
    assert greatest_common_divisor(16, 32) == 16

    assert greatest_common_divisor(58, 12) != 1
