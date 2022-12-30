from math import ceil as _ceil
from math import pi as _pi

from typing import Union as _Union

from ._vector import Vector as _Vector
from ._curve import Curve as _Curve
from ._screen import ScreenFacade as _ScreenFacade

_TNumber = _Union[int, float]


class ScreenConfiguration:
    """Defines the configuration for the plotter screen.

    Parameters
    ----------
    window_title : str
        Title to display on window. Defaults to "Curvipy".
    background_color : str
        Background color. Can either be a name or a hex color code. Defaults to "#FFFFFF".
    window_width : int or None
        Width of the screen window (in pixels). If None, `window_width` equals to 50% of the \
        display width. Defaults to None.
    window_height : int or None
        Height of the screen window (in pixels). If None, `window_height` equals to 75% of \
        the display height. Defaults to None.
    logical_width : int
        Logical width of the screen. This is the width that `Plotter` will operate with.
        While `window_width` is the real width of the screen, `logical_width` is a virtual \
        representation of it.
    logical_height : int
        Logical height of the screen. This is the height that `Plotter` will operate with.
        While `window_height` is the real height of the screen, `logical_height` is a virtual \
        representation of it.
    """

    def __init__(
        self,
        window_title: str = "Curvipy",
        background_color: str = "#FFFFFF",
        window_width: _Union[int, None] = None,
        window_height: int = None,
        logical_width: int = 20,
        logical_height: int = 20,
    ):
        self.window_title = window_title
        self.background_color = background_color
        self.window_width = window_width
        self.window_height = window_height
        self.logical_width = logical_width
        self.logical_height = logical_height


class PlottingConfiguration:
    """Defines the configuration for plotting curves and vectors.
        
    Parameters
    ----------
    plotting_speed : int
        Curve plotting speed. Integer from 1 to 10. Defaults to 10.
    curve_color : str
        Curve color. Can either be a name or a hex color code. Defaults to "#457B9D".
    curve_width : int
        Curve width. Defaults to 4.
    vector_color : str
        Vector color. Can either be a name or a hex color code. Defaults to "#E63946".
    vector_width : int
        Vector width. Defaults to 3.
    vector_head_size : int
        Size of vectors' head. Defaults to 10.
    show_vector_values : bool
        When True, vector head and tail values are shown on the axes. Defaults to True.
    vector_values_line_color : str
        Color of the dashed line drawn from the vector head and tail to the axes when \
        `show_vector_values` is set to True. Defaults to "#70CBCE".
    vector_values_line_width : int
        Width of the dashed line drawn from the vector head and tail to the axes. when \
        `show_vector_values` is set to True. Defaults to 3.
    """

    def __init__(
        self,
        plotting_speed: int = 10,
        curve_color: str = "#457B9D",
        curve_width: int = 4,
        vector_color: str = "#E63946",
        vector_width: int = 3,
        vector_head_size: int = 10,
        show_vector_values: bool = True,
        vector_values_line_color: str = "#70CBCE",
        vector_values_line_width: int = 3,
    ):
        # General attributes
        self.plotting_speed = plotting_speed

        # Curves attributes
        self.curve_color = curve_color
        self.curve_width = curve_width

        # Vectors
        self.vector_color = vector_color
        self.vector_width = vector_width
        self.vector_head_size = vector_head_size
        self.show_vector_values = show_vector_values
        self.vector_values_line_color = vector_values_line_color
        self.vector_values_line_width = vector_values_line_width


class AxesConfiguration:
    """Defines the configuration for the plotter axes.
        
    Parameters
    ----------
    show_axes : bool
        If true, x-axis and y-axis are shown. Defaults to True.
    axes_color : str
        Axis color. Can either be a name  or a hex color code. Defaults to "#70CBCE".
    axes_width : int
        Axis width. Defaults to 2.
    x_axis_scale : int or float
        Real value to define x-axis scale. Defaults to 1.
    y_axis_scale : int or float
        Real value to define y-axis scale. Defaults to 1.
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
        Ticks text color. Can either be a name or a hex color code. Defaults to "#000000".
    x_axis_tick_number_align : str
        Can either be "top" or "down". Defines if the x-axis ticks number will be placed \
        upside or downside the y-axis. Defaults to "down".
    y_axis_tick_number_align : str
        Can either be "left" or "right". Defines if the y-axis ticks number will be placed \
        to the left or to the right of the x-axis. Defaults to "left".
    """

    def __init__(
        self,
        show_axes: bool = True,
        axes_color: str = "#70CBCE",
        axes_width: int = 2,
        x_axis_scale: _TNumber = 1,
        y_axis_scale: _TNumber = 1,
        x_axis_ticks: int = 10,
        y_axis_ticks: int = 10,
        x_axis_tick_decimals: int = 2,
        y_axis_tick_decimals: int = 2,
        tick_number_font: tuple[str, str, str] = ("Verdana", 8, "normal"),
        tick_number_color: str = "#000000",
        x_axis_tick_number_align: str = "down",
        y_axis_tick_number_align: str = "left",
    ):
        self.show_axes = show_axes
        self.axes_color = axes_color
        self.axes_width = axes_width
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


class Plotter:
    """Graph plotter for drawing curves and vectors.

    Parameters
    ----------
    screen_config : ScreenConfiguration
        Screen configuration. By default, `screen_config` takes the defaults attributes \
        values of `ScreenConfiguration`.
    plotting_config : PlottingConfiguration
        Plotting configuration. By default, `plotting_config` takes the defaults attributes \
        values of `PlottingConfiguration`.
    axes_config : AxesConfiguration
        Axes configuration.  By default, `axes_config` takes the defaults attributes values \
        of `AxesConfiguration`.
    """

    def __init__(
        self,
        screen_config: ScreenConfiguration = None,
        plotting_config: PlottingConfiguration = None,
        axes_config: AxesConfiguration = None,
    ) -> None:
        if screen_config is not None:
            self.screen_config = screen_config
        else:
            self.screen_config = ScreenConfiguration()

        if plotting_config is not None:
            self.plotting_config = plotting_config
        else:
            self.plotting_config = PlottingConfiguration()

        if axes_config is not None:
            self.axes_config = axes_config
        else:
            self.axes_config = AxesConfiguration()

        self.__screen = _ScreenFacade(
            self.screen_config.window_title,
            self.screen_config.background_color,
            self.screen_config.window_width,
            self.screen_config.window_height,
            self.screen_config.logical_width,
            self.screen_config.logical_height,
        )

        if self.axes_config.show_axes:
            self._draw_axis()

    def _draw_axis(self) -> None:
        w, h = self.screen_config.logical_width, self.screen_config.logical_height

        # Y-AXIS
        ## Draw y-axis line
        self.__screen.draw_line(
            (0, -h / 2),
            (0, h / 2),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        ## Draw y-axis ticks
        dy = (
            0
            if not self.axes_config.y_axis_ticks
            else h / (self.axes_config.y_axis_ticks * 2)
        )

        if self.axes_config.y_axis_scale > 0:
            i_range = range(self.axes_config.y_axis_ticks * 2)
        else:
            i_range = range(self.axes_config.y_axis_ticks * 2, 0, -1)

        for i in i_range:
            y = dy * (i - self.axes_config.y_axis_ticks)
            if y == 0:
                continue
            self.draw_y_tick(y / self.axes_config.y_axis_scale)

        ## Draw y-axis line arrow
        axis_arrow_pos = (
            (0, h / 2) if self.axes_config.y_axis_scale > 0 else (0, -h / 2)
        )
        axis_arrow_ang = 0.5 * _pi if self.axes_config.y_axis_scale > 0 else -0.5 * _pi
        self.__screen.draw_arrow(
            point=axis_arrow_pos,
            arrow_angle=axis_arrow_ang,
            arrow_size=10,
            arrow_width=self.axes_config.axes_width,
            arrow_color=self.axes_config.axes_color,
            drawing_speed=self.__screen.MAX_DRAWING_SPEED,
        )

        # X-AXIS
        ## Draw x-axis line
        self.__screen.draw_line(
            (-w / 2, 0),
            (w / 2, 0),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        ## Draw x-axis ticks
        dx = (
            0
            if not self.axes_config.x_axis_ticks
            else w / (self.axes_config.x_axis_ticks * 2)
        )

        if self.axes_config.x_axis_scale > 0:
            i_range = range(self.axes_config.x_axis_ticks * 2)
        else:
            i_range = range(self.axes_config.x_axis_ticks * 2, 0, -1)

        for i in i_range:
            x = dx * (i - self.axes_config.x_axis_ticks)
            if x == 0:
                continue
            self.draw_x_tick(x / self.axes_config.x_axis_scale)

        ## Draw x-axis line arrow
        point = (w / 2, 0) if self.axes_config.x_axis_scale > 0 else (-w / 2, 0)
        axis_arrow_ang = 0 if self.axes_config.x_axis_scale > 0 else _pi
        self.__screen.draw_arrow(
            point=point,
            arrow_angle=axis_arrow_ang,
            arrow_size=10,
            arrow_width=self.axes_config.axes_width,
            arrow_color=self.axes_config.axes_color,
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
        # Values for `y_offset`, `text_offset` and `tick_length` have been determined
        # experimentally. This method work properly for small values of text font size
        # and well spaced ticks. If the given font is too big or ticks are drawn relative
        # closely, this method might overlap the ticks with their self or with the axes.

        # Variables setup
        w, h = self.screen_config.logical_width, self.screen_config.logical_height
        font_size = self.axes_config.tick_number_font[1]
        number_str = str(round(number, self.axes_config.x_axis_tick_decimals))

        # Offsets
        align = self.axes_config.x_axis_tick_number_align if not align else align
        if align == "down":
            y_offset = -0.04 * h  # -4% of the y-axis length
        if align == "up":
            y_offset = 0.02 * h  # 2% of the y-axis length

        text_offset = -font_size * len(number_str) * w * 0.5e-3

        # Draw x tick
        tick_length = 0.01 * h  # 1% of the y-axis length
        x = number * self.axes_config.x_axis_scale
        self.__screen.draw_line(
            (x, -tick_length),
            (x, tick_length),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(x + text_offset, 0 + y_offset),
            text_font=self.axes_config.tick_number_font,
            text_color=self.axes_config.tick_number_color,
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
        # Values for `y_offset`, `x_offset`, `tick_length` and `tick_length` have been
        # determined experimentally. This method work properly for small values of text
        # font size and well spaced ticks. If the given font is too big or ticks are drawn
        # relative closely, this method might overlap the ticks with their self or with the
        # axes.

        # Variables setup
        w, h = self.screen_config.logical_width, self.screen_config.logical_height
        font_size = self.axes_config.tick_number_font[1]
        number_str = str(round(number, self.axes_config.y_axis_tick_decimals))

        # Offsets
        align = self.axes_config.y_axis_tick_number_align if not align else align
        if align == "left":
            text_offset = font_size * len(number_str) * w * 1e-3
            x_offset = -0.02 * w - text_offset  # 2% of x-axis length plus text offset
        if align == "right":
            x_offset = 0.02 * w  # 2% of x-axis length

        y_offset = -font_size * h * 1e-3

        # Draw y tick
        tick_length = 0.01 * w  # 1% of the x-axis length
        y = number * self.axes_config.y_axis_scale
        self.__screen.draw_line(
            (-tick_length, y),
            (tick_length, y),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(0 + x_offset, y + y_offset),
            text_font=self.axes_config.tick_number_font,
            text_color=self.axes_config.tick_number_color,
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
            vector.tail[0] * self.axes_config.x_axis_scale,
            vector.tail[1] * self.axes_config.y_axis_scale,
        )
        scaled_head = (
            vector.head[0] * self.axes_config.x_axis_scale,
            vector.head[1] * self.axes_config.y_axis_scale,
        )
        scaled_vector = _Vector(scaled_head, scaled_tail)

        # Draw vector
        self.__screen.draw_line(
            scaled_tail,
            scaled_head,
            self.plotting_config.vector_width,
            self.plotting_config.vector_color,
            self.plotting_config.plotting_speed,
        )

        # Draw vector head
        self.__screen.draw_arrow(
            point=scaled_head,
            arrow_angle=scaled_vector.angle,
            arrow_size=self.plotting_config.vector_head_size,
            arrow_width=self.plotting_config.vector_width,
            arrow_color=self.plotting_config.vector_color,
            drawing_speed=self.__screen.MAX_DRAWING_SPEED,
        )

    def plot_curve(self, curve: _Curve) -> None:
        """Plots the given two-dimensional curve in the specified interval.

        Parameters
        ----------
        curve : Curve
            Curve to be plotted.
        """
        # Curve points
        scaled_points = [
            (
                self.axes_config.x_axis_scale * point[0],
                self.axes_config.y_axis_scale * point[1],
            )
            for point in curve.points()
        ]
        # Draw curve
        self.__screen.draw_polyline(
            scaled_points,
            self.plotting_config.curve_width,
            self.plotting_config.curve_color,
            self.plotting_config.plotting_speed,
        )

    def plot_animated_curve(self, curve: _Curve, samples_per_vector: int) -> None:
        """Plots the given curve by drawing a set of vectors pointing at the curve \
        points and then joining the vector heads.

        Parameters
        ----------
        curve : Curve
            Curve to be plotted.
        samples_per_vector : int
            Number of samples per each vector plotted. The less `samples_per_vector` \
            is, the more vectors are drawn. 
        """
        # Plot vectors:
        for i, vector in enumerate(curve.points()):
            if i % samples_per_vector != 0:
                continue

            self.plot_vector(_Vector(vector))

        # Plot curve:
        self.plot_curve(curve)

    def clean(self) -> None:
        """Removes curves and vectors plotted."""
        self.__screen.clean()
        if self.axes_config.show_axes:
            self._draw_axis()

    def wait(self) -> None:
        """Waits until plotter screen is clicked. When clicked, exits plotter."""
        self.__screen.exit_on_click()
