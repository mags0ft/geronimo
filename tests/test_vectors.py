"""
Test cases for the Vector class.
"""

import math
from geronimo.geometry.point import Point
from geronimo.geometry.vector import Vector


def test_different_dimensions() -> None:
    """
    Test for different Vector dimension sizes from 2 to 1023.
    """

    for dimensions in range(2, 1024):
        vec = Vector(dimensions=dimensions)
        assert vec.dimensions() == dimensions
        assert len(vec.values) == dimensions


def test_init_zero() -> None:
    """
    Tests if Vectors are initialized with 0 as values if not specified
    differently.
    """

    vec = Vector(dimensions=3)
    assert all(el == 0.0 for el in vec.values)


def test_length() -> None:
    """
    Tests if the length of vectors is calculated correctly.
    """

    vec = Vector([2, 0, 0])
    assert vec.length() == 2.0

    values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    vec = Vector(values)
    assert vec.length() == math.sqrt(sum(el**2 for el in values))


def test_scaling() -> None:
    """
    Tests simple scaling of Vectors by floats.
    """

    vec = Vector([1, 0, 0])
    vec = vec * 2.0
    assert vec.length() == 2.0 and vec.values[0] == 2.0


def test_dot_product() -> None:
    """
    Tests the dot product operation.
    """

    a, b = Vector([1, 2, 3]), Vector([3, 2, 1])
    assert a * b == 10.0


def test_from_two_points() -> None:
    """
    Tests constructing a vector from two points.
    """

    origin, tip = Point([1, 2, 4]), Point([4, 6, 8])
    vec = Vector.from_points(origin, tip)
    assert vec.values == [3, 4, 4]


def test_parallel() -> None:
    """
    Tests if two vectors are parallel.
    """

    a, b = Vector([1, 2, 4]), Vector([2, 4, 8])
    assert a.is_parallel(b)
    assert b.is_parallel(a)

    assert a.is_parallel(a)
    assert b.is_parallel(b)

    a, b = Vector([0, 4, 2]), Vector([8, 1, 2])
    assert not a.is_parallel(b)
    assert not b.is_parallel(a)

    assert a.is_parallel(a)
    assert b.is_parallel(b)


def test_get_scalar() -> None:
    """
    Tests the `Vector.get_scalar` function.
    """

    a, b = Vector([2, 4, 6]), Vector([4, 8, 12])
    assert a.get_scalar(b) == 0.5
    assert b.get_scalar(a) == 2

    a, b = Vector([1, 8, 4]), Vector([0, 6, 2])
    try:
        a.get_scalar(b)
        assert False  # We haven't thrown a ValueError yet? That's wrong!
    except ValueError:
        pass

    try:
        b.get_scalar(a)
        assert False
    except ValueError:
        pass

    try:
        a.get_scalar(b, check_uniform_scalar=False)
        assert False  # That's a division by zero!
    except ZeroDivisionError:
        pass

    assert b.get_scalar(a, check_uniform_scalar=False) == 0
