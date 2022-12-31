import turtle as _turtle

from math import sqrt as _sqrt
from math import sin as _sin
from math import cos as _cos
from math import pi as _pi

from typing import Union as _Union

_TNumber = _Union[int, float]
_TLogicalPoint = tuple[_TNumber, _TNumber]
_TRealPoint = tuple[_TNumber, _TNumber]


class ScreenFacade:
    """Screen with a virtual system of coordinates for drawing figures such as lines, polylines, \
    arrows and more. It encapsulates the turtle package functionalities. 
    
    `ScreenFacade` lets the users define a logical (or virtual) screen size by translating the given \
    logical points (a screen position with user virtual coordinates) to a real point (the actual \
    coordinates of the given point).

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
        Logical width of the screen. This is the width that the users of `ScreenFacade` class \
        will operate with.
        While `window_width` is the real width of the screen, `logical_width` is a virtual \
        representation of it.
    logical_height : int
        Logical height of the screen. This is the height that the users of `ScreenFacade` class \
        will operate with.
        While `window_height` is the real height of the screen, `logical_height` is a virtual \
        representation of it.
    """

    MIN_DRAWING_SPEED = 1
    MAX_DRAWING_SPEED = 10

    def __init__(
        self,
        window_title: str,
        background_color: str,
        window_width: int,
        window_height: int,
        logical_width: int,
        logical_height: int,
    ):
        # Screen setup
        self.__screen = _turtle.Screen()
        if window_width and window_height:
            self.__screen.setup(window_width, window_height)
        self.__screen.clear()
        self.__screen.title(window_title)
        self.__screen.bgcolor(background_color)
        self.background_color = background_color

        self.logical_width = logical_width
        self.logical_height = logical_height

        # Pen setup
        self.__pen = _turtle.Turtle(visible=False)

        # Performance attributes
        self.__pen_width_cache = None
        self.__pen_color_cache = None

    def get_screen_size(self) -> tuple[int, int]:
        """Returns the real width and height of the screen minus an offset.

        The offset is used to fix `turtle.Screen.window_width()` and \
        `turtle.Screen.window_height()` precision.
        """
        width_offset = 65
        height_offset = 65
        width = self.__screen.window_width()
        height = self.__screen.window_height()
        return width - width_offset, height - height_offset

    def get_real_point(self, logical_point: _TLogicalPoint) -> _TRealPoint:
        """Translates the given logical point to a real point.

        Parameters
        ----------
        logical_point : tuple[int or float, int or float]
            Virtual position to be translated.

        Returns
        -------
        tuple[int or float, int or float]
            Translated real position.
        """
        real_width, real_height = self.get_screen_size()
        return (
            logical_point[0] * (real_width / self.logical_width),
            logical_point[1] * (real_height / self.logical_height),
        )

    def goto_drawing(self, point: _TRealPoint, drawing_speed: int) -> None:
        """Moves pen to the given real point leaving a trace.

        Parameters
        ----------
        point : tuple[int or float, int or float]
            Point (real position) to which the pen will go leaving a trace.
        drawing_speed : int
            Speed at which the pen will move. Integer from 1 to 10.
        """
        self.__pen.down()
        self.__pen.speed(drawing_speed)
        self.__pen.goto(point)

    def goto_without_drawing(self, point: _TRealPoint, drawing_speed: int) -> None:
        """Moves pen to the given real point without leaving a trace.

        Parameters
        ----------
        point : tuple[int or float, int or float]
            Point (real position) to which the pen will go.
        drawing_speed : int
            Speed at which the pen will move. Integer from 1 to 10.
        """
        self.__pen.up()
        self.__pen.speed(drawing_speed)
        self.__pen.goto(point)

    def draw_line(
        self,
        start_point: _TLogicalPoint,
        end_point: _TLogicalPoint,
        line_width: int,
        line_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a line from start position to end position.

        Parameters
        ----------
        start_point : tuple[int or float, int or float]
            Logical position at which the line starts. `start_point` is \
            translated to a real position.
        end_point : tuple[int or float, int or float]
            Logical position at which the line ends. `end_point` is \
            translated to a real position.
        line_width : int
            Line width.
        line_color : str
            Line color.
        drawing_speed : int
            Drawing speed. Integer from 1 to 10.
        """
        # Pen setup
        if line_width != self.__pen_width_cache:
            self.__pen.width(line_width)
            self.__pen_width_cache = line_width

        if line_color != self.__pen_color_cache:
            self.__pen.color(line_color)
            self.__pen_color_cache = line_color

        # Go to first line point without drawing
        rstart_point = self.get_real_point(start_point)
        self.goto_without_drawing(rstart_point, __class__.MAX_DRAWING_SPEED)
        # Draw line
        rend_point = self.get_real_point(end_point)
        self.goto_drawing(rend_point, drawing_speed)

    def draw_polyline(
        self,
        points: list[_TLogicalPoint],
        polyline_width: int,
        polyline_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a polyline by joining the given points.

        Parameters
        ----------
        points : list[tuple[int or float, int or float]]
            List of the logical position of the polyline points.
        polyline_width : int
            Polyline width.
        polyline_color : str
            Polyline color.
        drawing_speed : int
            Drawing speed. Integer from 1 to 10.
        """
        # Pen setup
        if polyline_width != self.__pen_width_cache:
            self.__pen.width(polyline_width)
            self.__pen_width_cache = polyline_width

        if polyline_color != self.__pen_color_cache:
            self.__pen.color(polyline_color)
            self.__pen_color_cache = polyline_color

        # Variables
        rpoints = [self.get_real_point(point) for point in points]

        # Go to first polyline point without drawing
        self.__pen.speed(__class__.MAX_DRAWING_SPEED)
        self.__pen.up()
        self.__pen.goto(rpoints[0])
        # Draw polyline
        self.__pen.speed(drawing_speed)
        self.__pen.down()
        for rpoint in rpoints[1:]:
            self.__pen.goto(rpoint)

    def draw_arrow(
        self,
        point: _TLogicalPoint,
        arrow_size: int,
        arrow_angle: _TNumber,
        arrow_width: int,
        arrow_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws an arrow `>` at the given point.

        Parameters
        ----------
        point : tuple[int or float, int or float]
            Logical position where the arrow will be drawn.
        arrow_size : int
            Size of the arrow.
        arrow_angle : str
            Angle in radians. Indicates arrow direction.
        arrow_width : int
            Width of the arrow.
        arrow_color : str
            Color of the arrow.
        drawing_speed : int
            Drawing speed. Integer from 1 to 10.
        """
        # Pen setup
        self.__pen.width(arrow_width)
        self.__pen.color(arrow_color)

        # Variables setup
        rpoint = self.get_real_point(point)

        # Draw vector head
        left_arrow = (
            arrow_size * _cos(arrow_angle + _pi * 5 / 4),
            arrow_size * _sin(arrow_angle + _pi * 5 / 4),
        )
        left_arrow_endpoint = (
            rpoint[0] + left_arrow[0],
            rpoint[1] + left_arrow[1],
        )

        self.goto_without_drawing(rpoint, __class__.MAX_DRAWING_SPEED)
        self.goto_drawing(left_arrow_endpoint, drawing_speed)

        right_arrow = (
            arrow_size * _cos(arrow_angle - _pi * 5 / 4),
            arrow_size * _sin(arrow_angle - _pi * 5 / 4),
        )
        right_arrow_endpoint = (
            rpoint[0] + right_arrow[0],
            rpoint[1] + right_arrow[1],
        )

        # Draw arrow left size
        self.goto_without_drawing(rpoint, __class__.MAX_DRAWING_SPEED)
        self.goto_drawing(right_arrow_endpoint, drawing_speed)

    def draw_text(
        self,
        text: str,
        point: _TLogicalPoint,
        text_font: tuple[str, str, str],
        text_color: str,
        align: str,
    ) -> None:
        """Display the given text at the specified point.

        Parameters
        ----------
        text : str
            Text to be displayed.
        point : tuple[int or float, int or float]
            Logical position where the text will be drawn.
        text_font : tuple[str, str, str]
            A triple (fontname, fontsize, fonttype).
        text_color : str
            Text color.
        align : str
            Text alignment.
        """
        # Pen setup
        if text_color != self.__pen_color_cache:
            self.__pen.color(text_color)
            self.__pen_color_cache = text_color

        # Draw text
        rpoint = self.get_real_point(point)
        self.__pen.speed(__class__.MAX_DRAWING_SPEED)
        self.__pen.up()
        self.__pen.goto(rpoint)
        self.__pen.write(text, move=False, align=align, font=text_font)

    def clean(self) -> None:
        """Removes all drawings from screen."""
        self.__screen.clear()
        self.__screen.bgcolor(self.background_color)

    def exit_on_click(self):
        """Exits screen when clicked."""
        self.__screen.exitonclick()
