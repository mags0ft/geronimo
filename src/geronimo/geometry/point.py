"""
Module for point definitions.
"""


class Point:
    """
    Abstraction for Points in n-dimensional space.
    """

    position: list[float] = []

    def __init__(self, position: list[float] = [], dimensions: int = 3):
        """
        Initialize a new point;
        """

        self.position = (
            position if position else [0.0 for _ in range(dimensions)]
        )

    def dimensions(self) -> int:
        """
        Get the dimensionality of the point.
        """

        return len(self.position)
