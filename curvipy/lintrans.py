"""
This module contains functions for modifying curves with linear transformations specified
as matrices.

Matrices used for the linear transformation have a 2x2 dimension and follow the same
structure as numpy arrays (using 2x2 numpy arrays as matrices will also work).
"""

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

    :param curve: parametrized curve
    :param matrix: linear transformation 2x2 matrix (same structure as numpy arrays)
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

    :param curve: parametrized curve to rotate
    :param angle: angle in radians

    :return: rotated curve.
    """
    rotation_matrix = (
        (math.cos(angle), math.sin(angle)),
        (math.sin(angle), math.cos(angle)),
    )

    return transform_curve(curve, rotation_matrix)


def scale_curve(curve: Callable, scalar: Union[float, int]) -> Callable:
    """
    Scales the given curve by the given scalar.

    :param curve: parametrized curve to scale
    :param scalar: scalar to scale curve

    :return: scaled curve
    """
    scaling_matrix = ((scalar, 0), (0, scalar))
    return transform_curve(curve, scaling_matrix)
