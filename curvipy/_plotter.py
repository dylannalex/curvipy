from math import ceil as _ceil
from math import pi as _pi

from typing import Union as _Union

from ._vector import Vector as _Vector
from ._curve import Curve as _Curve
from ._interval import Interval as _Interval
from ._screen import ScreenFacade as _ScreenFacade

_TNumber = _Union[int, float]


class Plotter:
    """Graph plotter for drawing vectors and curves. Inherits from `turtle.Turtle` \
    class.
        
    Parameters
    ----------
    window_title : str
        Title to display on window. Defaults to "curvipy".
    plotting_speed : int
        Curve plotting speed. Integer from 1 to 10. Defaults to 10.
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
    show_vector_values : bool
        When True, vector head and tail values are shown on the axes. Defaults to True.
    vector_values_line_color : str
        Color of the dashed line drawn from the vector head and tail to the axes when \
        `show_vector_values` is set to True. Defaults to "#64C2C6".
    vector_values_line_width : int
        Width of the dashed line drawn from the vector head and tail to the axes. when \
        `show_vector_values` is set to True. Defaults to 3.
    show_axis : bool
        If true, x-axis and y-axis are shown. Defaults to True.
    axis_color : str
        Axis color. Can either be a name (e.g. "Green") or a hex color code. Defaults \
        to "#A8DADC".
    axis_width : int
        Axis width. Defaults to 2.
    x_axis_scale : int
        Positive integer. Defaults to 10.
    y_axis_scale : int
        Positive integer. Defaults to 10.
    x_axis_ticks : int
        Positive integer. Defaults to 10.
    y_axis_ticks : int
        Positive integer. Defaults to 10.
    x_axis_tick_decimals : int
        Positive integer. Defaults to 2.
    y_axis_tick_decimals : int
        Positive integer. Defaults to 2. 
    tick_number_font : tuple[str, str, str]
        A triple (fontname, fontsize, fonttype). Defaults to ("Verdana", 8, "normal"). 
    tick_number_color : str
        Ticks text color. Can either be a name (e.g. "Black") or a hex color code. Defaults \
        to "#000000".
    x_axis_tick_number_align : str
        Can either be "top" or "down". Defines if the x-axis ticks number will be placed \
        upside or downside the y-axis. Defaults to "down".
    y_axis_tick_number_align : str
        Can either be "left" or "right". Defines if the y-axis ticks number will be placed \
        to the left or to the right of the x-axis. Defaults to "left".
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
        show_vector_values: bool = True,
        vector_values_line_color: str = "#64C2C6",
        vector_values_line_width: int = 3,
        show_axis: bool = True,
        axis_color: str = "#A8DADC",
        axis_width: int = 2,
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
        x_axis_ticks: int = 10,
        y_axis_ticks: int = 10,
        x_axis_tick_decimals: int = 2,
        y_axis_tick_decimals: int = 2,
        tick_number_font: tuple[str, str, str] = ("Verdana", 8, "normal"),
        tick_number_color: str = "#000000",
        x_axis_tick_number_align: str = "down",
        y_axis_tick_number_align: str = "left",
    ) -> None:
        # Screen attributes
        self.__screen = _ScreenFacade(window_title, background_color)
        self.plotting_speed = plotting_speed

        # Curves attributes
        self.curve_color = curve_color
        self.curve_width = curve_width

        # Vectors attributes
        self.vector_color = vector_color
        self.vector_width = vector_width
        self.vector_head_size = vector_head_size
        self.show_vector_values = show_vector_values
        self.vector_values_line_color = vector_values_line_color
        self.vector_values_line_width = vector_values_line_width

        # Axis attributes
        self.axis_color = axis_color
        self.show_axis = show_axis
        self.axis_width = axis_width
        self.x_axis_scale = x_axis_scale
        self.y_axis_scale = y_axis_scale
        self.x_axis_ticks = x_axis_ticks
        self.y_axis_ticks = y_axis_ticks
        self.x_axis_tick_decimals = x_axis_tick_decimals
        self.y_axis_tick_decimals = y_axis_tick_decimals
        self.tick_number_font = tick_number_font
        self.tick_number_color = tick_number_color
        self.x_axis_tick_number_align = x_axis_tick_number_align
        self.y_axis_tick_number_align = y_axis_tick_number_align

        if self.show_axis:
            self._draw_axis()

    def _draw_axis(self) -> None:
        screen_size = self.__screen.get_screen_size()
        w, h = (screen_size[0] * 1.5, screen_size[1] * 1.5)

        # y axis
        self.__screen.draw_line(
            (0, -h),
            (0, h),
            self.axis_width,
            self.axis_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        dy = None if not self.y_axis_ticks else _ceil(h / self.y_axis_ticks)
        for i in range(self.y_axis_ticks * 2):
            y = dy * (i - self.y_axis_ticks)
            if y == 0:
                continue
            self.draw_y_tick(y / self.y_axis_scale)

        self.__screen.draw_arrow(
            point=(0, h),
            arrow_angle=0.5 * _pi,
            arrow_size=10,
            arrow_width=self.axis_width,
            arrow_color=self.axis_color,
            drawing_speed=self.__screen.MAX_DRAWING_SPEED,
        )

        # x axis
        self.__screen.draw_line(
            (-w, 0),
            (w, 0),
            self.axis_width,
            self.axis_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        dx = None if not self.x_axis_ticks else _ceil(w / self.x_axis_ticks)
        for i in range(self.x_axis_ticks * 2):
            x = dx * (i - self.x_axis_ticks)
            if x == 0:
                continue
            self.draw_x_tick(x / self.x_axis_scale)

        self.__screen.draw_arrow(
            point=(w, 0),
            arrow_angle=0,
            arrow_size=10,
            arrow_width=self.axis_width,
            arrow_color=self.axis_color,
            drawing_speed=self.__screen.MAX_DRAWING_SPEED,
        )

    def draw_x_tick(self, number: _TNumber, align: str = None) -> None:
        """Draws a tick on the x-axis.

        Parameters
        ----------
        number : int or float
            Tick number.
        align : str
            Can either be "top" or "down". Defines if the x-axis tick number will be placed \
            upside or downside the y-axis. If `None`, align takes \
            `Plotter.x_axis_tick_number_align` attribute value. Defaults to `None`.
        """
        font_size = self.tick_number_font[1]
        number_str = str(round(number, self.x_axis_tick_decimals))

        # Offsets
        align = self.x_axis_tick_number_align if not align else align
        if align == "down":
            y_offset = -20
        if align == "up":
            y_offset = 10

        x_offset = -font_size * len(number_str) // 2

        # Draw x tick
        x = number * self.x_axis_scale
        self.__screen.draw_line(
            (x, -5),
            (x, 5),
            self.axis_width,
            self.axis_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(x + x_offset, 0 + y_offset),
            text_font=self.tick_number_font,
            text_color=self.tick_number_color,
            align="left",
        )

    def draw_y_tick(self, number: _TNumber, align: str = None) -> None:
        """Draws a tick on the y-axis.

        Parameters
        ----------
        number : int or float
            Tick number.
        align : str
            Can either be "left" or "right". Defines if the y-axis ticks number will be placed \
            to the left or to the right of the x-axis. If `None`, align takes \
            `Plotter.y_axis_tick_number_align` attribute value. Defaults to `None`.
        """
        font_size = self.tick_number_font[1]
        number_str = str(round(number, self.y_axis_tick_decimals))

        # Offsets
        align = self.y_axis_tick_number_align if not align else align
        if align == "left":
            x_offset = -10 - font_size * len(number_str) * 0.8
        if align == "right":
            x_offset = 10

        y_offset = -font_size // 2

        # Draw y tick
        y = number * self.y_axis_scale
        self.__screen.draw_line(
            (-5, y),
            (5, y),
            self.axis_width,
            self.axis_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(0 + x_offset, y + y_offset),
            text_font=self.tick_number_font,
            text_color=self.tick_number_color,
            align="left",
        )

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

        # Compute scaled vector
        scaled_tail = (
            vector.tail[0] * self.x_axis_scale,
            vector.tail[1] * self.y_axis_scale,
        )
        scaled_head = (
            vector.head[0] * self.x_axis_scale,
            vector.head[1] * self.y_axis_scale,
        )
        scaled_vector = _Vector(scaled_head, scaled_tail)

        # Draw vector
        self.__screen.draw_line(
            scaled_tail,
            scaled_head,
            self.vector_width,
            self.vector_color,
            self.plotting_speed,
        )

        # Draw vector head
        self.__screen.draw_arrow(
            point=scaled_head,
            arrow_angle=scaled_vector.angle,
            arrow_size=self.vector_head_size,
            arrow_width=self.vector_width,
            arrow_color=self.vector_color,
            drawing_speed=self.__screen.MAX_DRAWING_SPEED,
        )

        # Show vector values
        if not self.show_vector_values:
            return
        dash_size = 2

        # Show vector tail values
        if scaled_tail[0] != 0:
            offset = 15 if scaled_tail[0] > 0 else -15
            total_dashes = abs(scaled_tail[0] // 20)
            self.__screen.draw_dashed_line(
                (0, scaled_tail[1]),
                (scaled_tail[0] - offset, scaled_tail[1]),
                total_dashes,
                dash_size,
                self.vector_values_line_width,
                self.vector_values_line_color,
                self.plotting_speed,
            )  # Horizontal dashed line

            offset = 15 if scaled_tail[1] > 0 else -15
            total_dashes = abs(scaled_tail[1] // 20)
            self.__screen.draw_dashed_line(
                (scaled_tail[0], scaled_tail[1] - offset),
                (scaled_tail[0], 0),
                total_dashes,
                dash_size,
                self.vector_values_line_width,
                self.vector_values_line_color,
                self.plotting_speed,
            )  # Vertical dashed line

        if scaled_tail[0] != 0:
            align = "up" if vector.tail[0] < 0 else "down"
            self.draw_x_tick(vector.tail[0], align)
        align = "left" if vector.tail[0] > 0 else "right"
        self.draw_y_tick(vector.tail[1], align)

        if scaled_head[0] != 0:
            # Show vector head values
            offset = 15 if scaled_head[0] > 0 else -15
            total_dashes = abs(scaled_head[0] // 20)
            self.__screen.draw_dashed_line(
                (0, scaled_head[1]),
                (scaled_head[0] - offset, scaled_head[1]),
                total_dashes,
                dash_size,
                self.vector_values_line_width,
                self.vector_values_line_color,
                self.plotting_speed,
            )  # Horizontal dashed line

            offset = 15 if scaled_head[1] > 0 else -15
            total_dashes = abs(scaled_head[1] // 20)
            self.__screen.draw_dashed_line(
                (scaled_head[0], scaled_head[1] - offset),
                (scaled_head[0], 0),
                total_dashes,
                dash_size,
                self.vector_values_line_width,
                self.vector_values_line_color,
                self.plotting_speed,
            )  # Vertical dashed line

        if scaled_head[0] != 0:
            align = "up" if vector.head[0] < 0 else "down"
            self.draw_x_tick(vector.head[0], align)
        align = "left" if vector.head[0] > 0 else "right"
        self.draw_y_tick(vector.head[1], align)

    def plot_curve(self, curve: _Curve, interval: _Interval) -> None:
        """Plots the given two-dimensional curve in the specified interval.

        Parameters
        ----------
        curve : Curve
            Curve to be plotted.
        interval : Interval
            Interval from which the curve will be plotted.
        """
        # Curve points
        scaled_points = [
            (
                self.x_axis_scale * point[0],
                self.y_axis_scale * point[1],
            )
            for point in curve.points(interval)
        ]
        # Draw curve
        self.__screen.draw_polyline(
            scaled_points,
            self.curve_width,
            self.curve_color,
            self.plotting_speed,
        )

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
        self.__screen.clean()
        if self.show_axis:
            self._draw_axis()

    def wait(self) -> None:
        """Waits until plotter screen is clicked. When clicked, exits plotter."""
        self.__screen.exit_on_click()
