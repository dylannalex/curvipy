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
        display width.
    window_height : int or None
        Height of the screen window (in pixels). If None, `window_height` equals to 75% of \
        the display height.
    """

    def __init__(
        self,
        window_title: str = "Curvipy",
        background_color: str = "#FFFFFF",
        window_width: int = None,
        window_height: int = None,
    ):
        self.window_title = window_title
        self.background_color = background_color
        self.window_width = window_width
        self.window_height = window_height


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
    """

    def __init__(
        self,
        plotting_speed: int = 10,
        curve_color: str = "#457B9D",
        curve_width: int = 4,
        vector_color: str = "#E63946",
        vector_width: int = 3,
        vector_head_size: int = 10,
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


class AxesConfiguration:
    """Defines the configuration for the plotter axes.
        
    Parameters
    ----------
    show_axes : bool
        If True, x-axis and y-axis are shown. Defaults to True.
    show_axes_direction : bool
        If True, `Plotter` replaces the last tick of both axes with an arrow that \
        indicates the axis direction. Defaults to False.
    axes_color : str
        Axis color. Can either be a name  or a hex color code. Defaults to "#70CBCE".
    axes_width : int
        Axis width. Defaults to 2.
    ticks_font : tuple[str, str, str]
        A triple (fontname, fontsize, fonttype). Defaults to ("Verdana", 8, "normal"). 
    ticks_color : str
        Ticks text color. Can either be a name or a hex color code. Defaults to "#000000".
    x_ticks : int
        Number of ticks of half the x-axis, i.e. total x-axis ticks equals `2 * x_ticks`. \
        Defaults to 10.
    x_ticks_distance : int
        Distance between each x-axis tick. E.g. if `x_ticks_distance` equals 1, x-axis \
        ticks will be `{..., -2, -1, 0, 1, 2, ...}`. Defaults to 1.
    x_ticks_decimals : int
        Number of decimals of the x-axis ticks number. Defaults to 2.
    x_ticks_align : str
        Can either be "top" or "down". Defines if the x-axis ticks number will be placed \
        upside or downside the x-axis. Defaults to "down".
    x_ticks : int
        Number of ticks of half the y-axis, i.e. total y-axis ticks equals `2 * y_ticks`. \
        Defaults to 10.
    y_ticks_distance : int
        Distance between each y-axis tick. E.g. if `y_ticks_distance` equals 0.5, y-axis \
        ticks will be `{..., -1, -0.5, 0, 0.5, 1, ...}`. Defaults to 1.
    y_tick_decimals : int
        Number of decimals of the y-axis ticks number. Defaults to 2.
    y_ticks_align : str
        Can either be "left" or "right". Defines if the y-axis ticks number will be placed \
        to the left or to the right of the y-axis. Defaults to "left".
    """

    def __init__(
        self,
        show_axes: bool = True,
        show_axes_direction: bool = False,
        axes_color: str = "#70CBCE",
        axes_width: int = 2,
        ticks_font: tuple[str, str, str] = ("Verdana", 8, "normal"),
        ticks_color: str = "#000000",
        x_ticks: int = 10,
        x_ticks_distance: int = 1,
        x_ticks_decimals: int = 2,
        x_ticks_align: str = "down",
        y_ticks: int = 10,
        y_ticks_distance: int = 1,
        y_ticks_decimals: int = 2,
        y_ticks_align: str = "left",
    ):
        # General attributes
        self.show_axes = show_axes
        self.show_axes_direction = show_axes_direction
        self.axes_color = axes_color
        self.axes_width = axes_width
        self.ticks_font = ticks_font
        self.ticks_color = ticks_color
        # X-axis ticks attributes
        self.x_ticks = x_ticks
        self.x_ticks_distance = x_ticks_distance
        self.x_ticks_decimals = x_ticks_decimals
        self.x_ticks_align = x_ticks_align
        # Y-axis ticks attributes
        self.y_ticks = y_ticks
        self.y_ticks_distance = y_ticks_distance
        self.y_ticks_decimals = y_ticks_decimals
        self.y_ticks_align = y_ticks_align


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
        # Plotter coordinates system:
        #
        # `curvipy.Plotter` works with a virtual set of coordinates defined by the a logical width
        # and height. The logical screen size is independent of the real window size, and virtual
        # coordinates are translated to real window coordinates.
        # Despite setting a logical width and height do not affect the window size, it defines the
        # xy-plane coordinate system. This is useful for precisely calibrating the distance between
        # the axes ticks.
        #
        # Note that the x-axis length equals the logical width and the y-axis length equals the
        # logical height.
        #
        # If we want the x-axis to have `n` total ticks with a distance `Dx` between their self, that is
        #
        #                           axis_ticks = {Dx. i | i in N ^ -n/2 <= i <= n/2}
        #                                      = {..., -2.Dx, -Dx, 0, Dx, 2.Dx, ....}
        #
        # and the y-axis to have `m` total ticks with a distance `Dy` between their self, that is
        #
        #                           axis_ticks = {Dy. i | i in N ^ -m/2 <= i <= m/2}
        #                                      = {..., -2.Dy, -Dy, 0, Dy, 2.Dy, ....}
        #
        # then
        #
        #                                   logical_width = n . Dx
        #                                   logical_height = m . Dy
        #

        # Public attributes
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

        # Private attributes
        total_x_ticks = 2 * self.axes_config.x_ticks
        total_y_ticks = 2 * self.axes_config.y_ticks

        self.__logical_width = total_x_ticks * self.axes_config.x_ticks_distance
        self.__logical_height = total_y_ticks * self.axes_config.y_ticks_distance

        self.__screen = _ScreenFacade(
            self.screen_config.window_title,
            self.screen_config.background_color,
            self.screen_config.window_width,
            self.screen_config.window_height,
            self.__logical_width,
            self.__logical_height,
        )

        if self.axes_config.show_axes:
            self._draw_axis()

    def _draw_axis(self) -> None:
        w, h = self.__logical_width, self.__logical_height

        # Draw y-axis line
        self.__screen.draw_line(
            (0, -h / 2),
            (0, h / 2),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        # Draw y-axis ticks
        dy = 0 if not self.axes_config.y_ticks else h / (self.axes_config.y_ticks * 2)
        for i in range(self.axes_config.y_ticks * 2):
            y = dy * (i - self.axes_config.y_ticks)
            if y != 0:
                self.draw_y_tick(y)

        # Draw y-axis last tick or arrow (see `AxesConfiguration.show_axes_direction` attribute description)
        if self.axes_config.show_axes_direction:
            axis_arrow_pos = (0, h / 2)
            axis_arrow_ang = 0.5 * _pi
            self.__screen.draw_arrow(
                point=axis_arrow_pos,
                arrow_angle=axis_arrow_ang,
                arrow_size=10,
                arrow_width=self.axes_config.axes_width,
                arrow_color=self.axes_config.axes_color,
                drawing_speed=self.__screen.MAX_DRAWING_SPEED,
            )

        else:
            last_tick = dy * self.axes_config.y_ticks
            self.draw_y_tick(last_tick)

        # Draw x-axis line
        self.__screen.draw_line(
            (-w / 2, 0),
            (w / 2, 0),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )

        # Draw x-axis ticks
        dx = 0 if not self.axes_config.x_ticks else w / (self.axes_config.x_ticks * 2)
        for i in range(self.axes_config.x_ticks * 2):
            x = dx * (i - self.axes_config.x_ticks)
            if x != 0:
                self.draw_x_tick(x)

        # Draw x-axis last tick or arrow (see `AxesConfiguration.show_axes_direction` attribute description)
        if self.axes_config.show_axes_direction:
            axis_arrow_pos = (w / 2, 0)
            axis_arrow_ang = 0
            self.__screen.draw_arrow(
                point=axis_arrow_pos,
                arrow_angle=axis_arrow_ang,
                arrow_size=10,
                arrow_width=self.axes_config.axes_width,
                arrow_color=self.axes_config.axes_color,
                drawing_speed=self.__screen.MAX_DRAWING_SPEED,
            )
        else:
            last_tick = dx * self.axes_config.x_ticks
            self.draw_x_tick(last_tick)

    def draw_x_tick(self, number: _TNumber, align: str = None) -> None:
        """Draws a tick on the x-axis.

        Parameters
        ----------
        number : int or float
            Tick number.
        align : str
            Can either be "top" or "down". Defines if the x-axis tick number will be placed \
            upside or downside the y-axis. If `None`, align takes \
            `Plotter.x_ticks_align` attribute value. Defaults to `None`.
        """
        # NOTE: values for `y_offset`, `text_offset` and `tick_length` have been determined
        # experimentally. This method work properly for small values of text font size
        # and well spaced ticks. If the given font is too big or ticks are drawn relative
        # closely, this method might overlap the ticks with their self or with the axes.

        # Variables setup
        w, h = self.__logical_width, self.__logical_height
        font_size = self.axes_config.ticks_font[1]
        number_str = str(round(number, self.axes_config.x_ticks_decimals))

        # Offsets
        align = self.axes_config.x_ticks_align if not align else align
        if align == "down":
            y_offset = -0.04 * h  # -4% of the y-axis length
        if align == "up":
            y_offset = 0.02 * h  # 2% of the y-axis length

        text_offset = -font_size * len(number_str) * w * 0.5e-3

        # Draw x tick
        tick_length = 0.01 * h  # 1% of the y-axis length
        self.__screen.draw_line(
            (number, -tick_length),
            (number, tick_length),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(number + text_offset, 0 + y_offset),
            text_font=self.axes_config.ticks_font,
            text_color=self.axes_config.ticks_color,
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
            `Plotter.y_ticks_align` attribute value. Defaults to `None`.
        """
        # NOTE: values for `y_offset`, `x_offset`, `tick_length` and `tick_length` have been
        # determined experimentally. This method work properly for small values of text
        # font size and well spaced ticks. If the given font is too big or ticks are drawn
        # relative closely, this method might overlap the ticks with their self or with the
        # axes.

        # Variables setup
        w, h = self.__logical_width, self.__logical_height
        font_size = self.axes_config.ticks_font[1]
        number_str = str(round(number, self.axes_config.y_ticks_decimals))

        # Offsets
        align = self.axes_config.y_ticks_align if not align else align
        if align == "left":
            text_offset = font_size * len(number_str) * w * 1e-3
            x_offset = -0.02 * w - text_offset  # 2% of x-axis length plus text offset
        if align == "right":
            x_offset = 0.02 * w  # 2% of x-axis length

        y_offset = -font_size * h * 1e-3

        # Draw y tick
        tick_length = 0.01 * w  # 1% of the x-axis length
        self.__screen.draw_line(
            (-tick_length, number),
            (tick_length, number),
            self.axes_config.axes_width,
            self.axes_config.axes_color,
            self.__screen.MAX_DRAWING_SPEED,
        )
        self.__screen.draw_text(
            text=number_str,
            point=(0 + x_offset, number + y_offset),
            text_font=self.axes_config.ticks_font,
            text_color=self.axes_config.ticks_color,
            align="left",
        )

    def plot_vector(self, vector: _Vector) -> None:
        """Plots the given two-dimensional vector.

        Parameters
        ----------
        vector : Vector
            Vector to be plotted.
        """
        # NOTE: for plotting the vector arrow, we cannot use the vector angle because
        # the vector components do not reflect the real coordinates where it will be
        # drawn. Because of that, we need the angle of a scaled version of itself, that
        # reflect the real coordinates on screen of the vector.
        #
        # TODO:
        #   - Display vector components

        # Check if vector is the cero vector (v = [0, 0])
        if not vector.norm:
            return

        # Draw vector
        self.__screen.draw_line(
            vector.tail,
            vector.head,
            self.plotting_config.vector_width,
            self.plotting_config.vector_color,
            self.plotting_config.plotting_speed,
        )

        # Draw vector head
        scaled_vector = _Vector(self.__screen.get_real_point(vector.components))
        self.__screen.draw_arrow(
            point=vector.head,
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
        # Draw curve
        curve_points = curve.points()
        self.__screen.draw_polyline(
            curve_points,
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
