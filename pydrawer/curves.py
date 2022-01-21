from typing import Callable, Union
import math


def transform_curve(
    curve: Callable,
    matrix: tuple[
        tuple[Union[float, int], Union[float, int]],
        tuple[Union[float, int], Union[float, int]],
    ],
) -> Callable:
    """
    Applies a linear transformation (matrix) to a curve.

    curve(Callable):    parametrized curve
    matrix(Matrix):     matrix to transforme the curve
    """
    g = lambda t: curve(t)[0]
    m = lambda t: curve(t)[1]
    return lambda t: (
        g(t) * matrix[0][0] + m(t) * matrix[0][1],
        g(t) * matrix[1][0] + m(t) * matrix[1][1],
    )


def rotate_curve(curve: Callable, angle: Union[float, int]) -> Callable:
    """
    Rotates a curve anticlockwise by the given angle.

    curve(Callable):    parametrized curve to rotate
    angle(float, int):  angle in radians
    """
    rotation_matrix = (
        (math.cos(angle), math.cos(angle + math.pi / 4)),
        (math.sin(angle), math.sin(angle + math.pi / 4)),
    )

    return transform_curve(curve, rotation_matrix)


def scale_curve(curve: Callable, scalar: Union[float, int]) -> Callable:
    """
    Scales the given curve by the given scalar.

    curve(Callable):    parametrized curve to scale
    angle(float, int):  angle in radians
    """
    scaling_matrix = ((scalar, 0), (0, scalar))
    return transform_curve(curve, scaling_matrix)
