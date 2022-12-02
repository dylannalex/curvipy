import math as _math

class Vector3D:
    """Three-dimensional vector `v = (v1, v2, v3)`

    Attributes
    ----------
    head : tuple[int or float, int or float, int or float]
        Three-dimensional point at which the vector is pointing.
    tail : tuple[int or float, int or float, int or float]
        Three-dimensional point at which the vector starts.
    """

    def __init__(
        self,
        head: tuple[int | float, int | float, int | float],
        tail: tuple[int | float, int | float, int | float] = (0, 0), 
    ):
        self.head = head
        self.tail = tail

    @property
    def components(self) -> tuple[int | float, int | float, int | float]:
        return (self.head[0] - self.tail[0], self.head[1] - self.tail[1], self.head[2] - self.tail[2])
    
    @property
    def norm(self) -> float:
        """Norm of the vector."""
        return _math.sqrt(self.components[0] ** 2 + self.components[1] ** 2 + self.components[2] ** 2)
    
    @property
    def angles(self) -> tuple[float, float, float]:
        alpha = _math.acos(self.components[0] / self.norm)
        beta = _math.acos(self.components[1] / self.norm)
        gamma = _math.acos(self.components[2] / self.norm)

        if (self.components[1] < 0) and (self.components[2] < 0): alpha = -alpha
        if (self.components[0] < 0) and (self.components[2] < 0): beta = -beta
        if (self.components[1] < 0) and (self.components[0] < 0): gamma = -gamma

        return (alpha, beta, gamma)

    @property
    def xyprojection(self) -> tuple[int | float, int | float]:
        """Projection of the Vector on XY plane"""
        return (self.components[0], self.components[1])

    def __getitem__(self, i: int) -> int | float:
        return self.components[i]
    
    def __len__(self) -> int:
        return len(self.components)
