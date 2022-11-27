import math as _math


class Vector:
    """Two-dimensional vector `v = (v1, v2)`.

    Attributes
    ----------
    head : tuple[int or float, int or float]
        Two-dimensional point at which the vector is pointing.
    tail : tuple[int or float, int or float]
        Two-dimensional point at which the vector starts.
    """

    def __init__(
        self,
        head: tuple[int | float, int | float],
        tail: tuple[int | float, int | float] = (0, 0),
    ):
        self.head = head
        self.tail = tail

    @property
    def components(self) -> tuple[int | float, int | float]:
        return (self.head[0] - self.tail[0], self.head[1] - self.tail[1])

    @property
    def norm(self) -> float:
        """Norm of the vector."""
        return _math.sqrt(self.components[0] ** 2 + self.components[1] ** 2)

    @property
    def angle(self) -> float:
        """Angle between the vector and the x-axis in radians. This angle \
        is a real number in the interval [-π, π]. If the angle is positive \
        it indicates an anticlockwise rotation from the x-axis, this means \
        that the vector is on the first or the second quadrant. If the angle \
        is negative it indicates a clockwise rotation from the x-axis, this \
        means that the vector is on the third or fourth quadrant.
        """
        angle = _math.acos(self.components[0] / self.norm)
        return angle if self.components[1] >= 0 else -angle

    def __getitem__(self, i: int) -> int | float:
        return self.components[i]

    def __len__(self) -> int:
        return len(self.components)
