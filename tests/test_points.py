"""
Tests for the Point class in geronimo.
"""

from geronimo.geometry.point import Point


def test_different_dimensions() -> None:
    """
    Test for different Point dimension sizes from 2 to 1023.
    """

    for dimensions in range(2, 1024):
        pnt = Point(dimensions=dimensions)
        assert pnt.dimensions() == dimensions
        assert len(pnt.position) == dimensions


def test_init_zero() -> None:
    """
    Tests if Points are initialized with 0 as position if not specified
    differently.
    """

    pnt = Point(dimensions=3)
    assert all(el == 0.0 for el in pnt.position)


def test_init_and_read() -> None:
    """
    Tests if Points are indeed correctly initialized.
    """

    pnt = Point([2, 4, 6])
    assert pnt.position == [2, 4, 6]
