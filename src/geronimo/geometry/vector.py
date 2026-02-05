"""
Module for vector definitions.
"""

from math import sqrt
from typing import overload

from .point import Point


class Vector:
    """
    Generic class to represent a vector in an n-dimensional space.
    """

    values: list[float] = []  # stores the values

    def __init__(self, values: list[float] | None = None, dimensions: int = 3):
        """
        Initialize a new vector. If no values are given, fill it with n zeroes,
        where n is the number of dimensions (default: 3).
        """

        self.values = values if values else [0.0 for _ in range(dimensions)]

    def _dimension_check(self, other: "Vector") -> None:
        """
        Internal check to make sure two given vectors are of the same
        dimensionality.
        """

        if other.dimensions() == self.dimensions():
            return

        raise ValueError(
            "Vectors do not have the same dimension "
            f"({other.dimensions()} != {self.dimensions()})"
        )

    @staticmethod
    def from_points(origin: Point, tip: Point) -> "Vector":
        """
        Constructs a new Vector from two given points, the origin of the vector
        and its tip (e.g. target, where it points to).
        """

        if origin.dimensions() != tip.dimensions():
            raise ValueError("points need to have the same dimensions")

        return Vector([a - b for a, b in zip(tip.position, origin.position)])

    def length(self) -> float:
        """
        Get the length of the vector.
        """

        return sqrt(sum(el**2 for el in self.values))

    def __add__(self, other: "Vector") -> "Vector":
        """
        Adds two vectors together.
        """

        self._dimension_check(other)
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtracts two vectors from each other.
        """

        self._dimension_check(other)
        return Vector([a - b for a, b in zip(self.values, other.values)])

    @overload
    def __mul__(self, other: "Vector") -> float: ...

    @overload
    def __mul__(self, other: float | int) -> "Vector": ...

    def __mul__(self, other: "Vector | float | int") -> "Vector | float":
        """
        Compute the dot product of two vectors or scale the vector by a scalar.
        """

        if isinstance(other, Vector):
            self._dimension_check(other)
            return sum(a * b for a, b in zip(self.values, other.values))

        return Vector([d * other for d in self.values])

    def __repr__(self) -> str:
        """
        Representation of the vector.
        """

        return "Vector(" + ", ".join([str(el) for el in self.values]) + ")"

    def __str__(self) -> str:
        """
        Representation of the vector as a string.
        """

        return "<" + ", ".join([str(el) for el in self.values]) + ">"

    def is_perpendicular(self, other: "Vector") -> bool:
        """
        Check if two vectors are perpendicular to each other.
        """

        return self * other == 0

    def is_parallel(self, other: "Vector") -> bool:
        """
        Check if two given vectors are parallel.
        """

        self._dimension_check(other)
        k: float | None = None

        for val_a, val_b in zip(self.values, other.values):
            if val_b == 0:
                continue

            local_k = val_a / val_b

            if k is None:
                k = local_k
                continue

            if local_k != k:
                return False

        return True

    def get_scalar(
        self, other: "Vector", check_uniform_scalar: bool = True
    ) -> float:
        """
        Gets the scalar *λ* (also known as *k* or *r*) for two given vectors.
        If `check_uniform_scalar` is set to True, the function will check if
        the two vectors actually have a uniform scalar *λ* before returning it,
        otherwise raising a ValueError.

        It is recommended to leave `check_uniform_scalar` set to `True` at the
        expense of slightly more computational effort.
        """

        if check_uniform_scalar and not self.is_parallel(other):
            raise ValueError(
                "vectors are not parallel and cannot have uniform λ"
            )

        return self.values[0] / other.values[0]

    def dimensions(self) -> int:
        """
        Get the dimensionality of the vector.
        """

        return len(self.values)

    def normalize(self) -> "Vector":
        """
        Normalise the vector and return the result. Out-of-place.
        """

        coeff = 1 / self.length()

        return self * coeff  # type: ignore
