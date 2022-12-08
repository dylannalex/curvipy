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
        """Vector head point when tail is moved to the origin."""
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

    def __mul__(self, scalar: int | float) -> "Vector":
        """Defines vector scaling. The scaled vector is not placed at the \
        origin, that is, the scaled vector will preserve the vector tail.

        Example:
        ```
        v = curvipy.Vector(tail=[-1, -1], head=[2, 2])
        w = v * 2
        n = v * -1
        w.tail
        >>> (-1, -1)
        w.head
        >>> (5, 5)
        w.components
        >>> (6, 6)
        n.tail
        >>> (-1, -1)
        n.head
        >>> (-4, -4)
        n.components
        >>> (-3, -3)
        ```
        """
        scaled_vector_components = [
            self.components[0] * scalar,
            self.components[1] * scalar,
        ]
        scaled_vector_head = [
            self.tail[0] + scaled_vector_components[0],
            self.tail[1] + scaled_vector_components[1],
        ]
        return Vector(head=scaled_vector_head, tail=self.tail)

    def __add__(self, vector: "Vector") -> "Vector":
        """Defines vector addition. Result vector is placed at the origin, \
        that is, the tail of the result vector is (0, 0).

        Example:
        ```
        v = curvipy.Vector(tail=[-1, -1], head=[2, 2])
        w = curvipy.Vector(tail=[2, 0], head=[1, -2])
        n = v + w
        n.tail
        >>> (0, 0)
        n.head
        >>> (2, 1)
        ```
        """
        head = (
            self.components[0] + vector.components[0],
            self.components[1] + vector.components[1],
        )
        return Vector(head)

    def __sub__(self, vector: "Vector") -> "Vector":
        """Defines vector subtraction. Result vector is placed at the origin, \
        that is, the tail of the result vector is (0, 0).

        Example:
        ```
        v = curvipy.Vector(tail=[-1, -1], head=[2, 2])
        w = curvipy.Vector(tail=[2, 0], head=[1, -2])
        n = v - w
        n.tail
        >>> (0, 0)
        n.head
        >>> (4, 5)
        ```
        """
        return self + vector * -1
