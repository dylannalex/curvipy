import turtle as _turtle
from math import sin as _sin
from math import cos as _cos
from math import pi as _pi

from ._vector import Vector as _Vector
from ._curve import Curve as _Curve
from ._interval import Interval as _Interval


class Plotter(_turtle.Turtle):
    """Graph plotter for drawing vectors and curves. Inherits from `turtle.Turtle` \
    class.
        
    Parameters
    ----------
    window_title : str
        Title to display on window. Defaults to "curvipy".
    plotting_speed : int
        Curve plotting speed. Defaults to 11.
    background_color : str
        Background color. Can either be a name (e.g. "Blue") or a hex color code. \
        Defaults to "#F1FAEE".
    curve_color : str
        Curve color. Can either be a name (e.g. "Red") or a hex color code. Defaults \
        to "#457B9D".
    curve_width : int
        Curve width. Defaults to 4.
    vector_color : str
        Vector color. Can either be a name (e.g. "Yellow") or a hex color code. Defaults \
        to "#E63946".
    vector_width : int
        Vector width. Defaults to 3.
    vector_head_size : int
        Size of vectors' head. Defaults to 10.
    show_axis : bool
        If true, x-axis and y-axis are shown. Defaults to True.
    axis_color : str
        Axis color. Can either be a name (e.g. "Green") or a hex color code. Defaults \
        to "#A8DADC".
    axis_width : int
        Axis width. Defaults to 2.
    x_axis_scale : int
        X-axis scale. Defaults to 10.
    y_axis_scale : int
        Y-axis scale. Defaults to 10.
    """

    def __init__(
        self,
        window_title: str = "Curvipy",
        plotting_speed: int = 11,
        background_color: str = "#F1FAEE",
        curve_color: str = "#457B9D",
        curve_width: int = 4,
        vector_color: str = "#E63946",
        vector_width: int = 3,
        vector_head_size: int = 10,
        show_axis: bool = True,
        axis_color: str = "#A8DADC",
        axis_width: int = 2,
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:

        _turtle.Turtle.__init__(self)
        self.shapesize(0.1, 0.1, 0.1)
        self.shape("square")
        _turtle.title(window_title)
        _turtle.bgcolor(background_color)

        # Screen attributes
        self.plotting_speed = plotting_speed
        self.background_color = background_color

        # Curves attributes
        self.curve_color = curve_color
        self.curve_width = curve_width

        # Vectors attributes
        self.vector_color = vector_color
        self.vector_width = vector_width
        self.vector_head_size = vector_head_size

        # Axis attributes
        self.axis_color = axis_color
        self.show_axis = show_axis
        self.axis_width = axis_width
        self.x_axis_scale = x_axis_scale
        self.y_axis_scale = y_axis_scale

        if self.show_axis:
            self._draw_axis()

    def _goto_without_drawing(self, position: tuple[int, int]) -> None:
        self.speed("fastest")
        self.up()
        self.goto(position)
        self.down()

    def _goto_drawing(self, position: tuple[int, int]) -> None:
        self.speed(self.plotting_speed)
        self.down()
        self.goto(position)

    def _draw_axis(self) -> None:
        self.width(self.axis_width)
        self.color(self.axis_color)

        w, h = _turtle.screensize()

        # y axis
        self._goto_without_drawing((0, -h * 2))
        self.goto(0, h * 2)

        # x axis
        self._goto_without_drawing((-w * 2, 0))
        self.goto((w * 2, 0))

    def plot_vector(self, vector: _Vector) -> None:
        """Plots the given two-dimensional vector.

        Parameters
        ----------
        vector : Vector
            Vector to be plotted.
        """
        # Check if vector is the cero vector (v = [0, 0])
        if not vector.norm:
            return

        # Turtle settings
        self.color(self.vector_color)
        self.width(self.vector_width)

        # Draw vector
        scaled_tail = (
            vector.tail[0] * self.x_axis_scale,
            vector.tail[1] * self.y_axis_scale,
        )
        self._goto_without_drawing(scaled_tail)
        scaled_head = (
            vector.head[0] * self.x_axis_scale,
            vector.head[1] * self.y_axis_scale,
        )
        self._goto_drawing(scaled_head)

        # Draw vector head
        left_head_vector = (
            self.vector_head_size * _cos(vector.angle + _pi * 5 / 4),
            self.vector_head_size * _sin(vector.angle + _pi * 5 / 4),
        )
        left_head_endpoint = (
            scaled_head[0] + left_head_vector[0],
            scaled_head[1] + left_head_vector[1],
        )

        self._goto_drawing(left_head_endpoint)

        right_head_vector = (
            self.vector_head_size * _cos(vector.angle - _pi * 5 / 4),
            self.vector_head_size * _sin(vector.angle - _pi * 5 / 4),
        )
        right_head_endpoint = (
            scaled_head[0] + right_head_vector[0],
            scaled_head[1] + right_head_vector[1],
        )

        self._goto_without_drawing(scaled_head)
        self._goto_drawing(right_head_endpoint)

    def plot_curve(self, curve: _Curve, interval: _Interval) -> None:
        """Plots the given two-dimensional curve in the specified interval.

        Parameters
        ----------
        curve : Curve
            Curve to be plotted.
        interval : Interval
            Interval from which the curve will be plotted.
        """
        # Turtle settings
        self.color(self.curve_color)
        self.width(self.curve_width)

        # Curve points
        points = curve.points(interval)
        start_point = points[0]
        scaled_start_point = (
            self.x_axis_scale * start_point[0],
            self.y_axis_scale * start_point[1],
        )

        # Draw curve
        self._goto_without_drawing(scaled_start_point)
        for point in points[1:]:
            scaled_point = (
                self.x_axis_scale * point[0],
                self.y_axis_scale * point[1],
            )
            self._goto_drawing(scaled_point)

    def plot_animated_curve(
        self, curve: _Curve, interval: _Interval, samples_per_vector: int
    ) -> None:
        """Plots the given curve by drawing a set of vectors pointing at the curve \
        points and then joining the vector heads.

        Parameters
        ----------
        curve : Curve
            Curve to be plotted.
        interval : Interval
            Interval from which the curve will be plotted.
        samples_per_vector : int
            Number of samples per each vector plotted. The less `samples_per_vector` \
            is, the more vectors are drawn. 
        """
        # Plot vectors:
        for i, vector in enumerate(curve.points(interval)):
            if i % samples_per_vector != 0:
                continue

            self.plot_vector(_Vector(vector))

        # Plot curve:
        self.plot_curve(curve, interval)

    def clean(self) -> None:
        """Removes curves and vectors plotted."""
        self.clear()
        _turtle.bgcolor(self.background_color)
        if self.show_axis:
            self._draw_axis()
