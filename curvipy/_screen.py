import turtle as _turtle

from math import sin as _sin
from math import cos as _cos
from math import pi as _pi

from typing import Union as _Union

_TNumber = _Union[int, float]
_TPoint = tuple[_TNumber, _TNumber]


class ScreenFacade:
    """Draw figures such as lines and polylines.

    ScreenFacade encapsulates the turtle package functionalities.

    Parameters
    ----------
    window_title : str
    background_color : str
    """

    MIN_DRAWING_SPEED = 1
    MAX_DRAWING_SPEED = 10

    def __init__(self, window_title: str, background_color: str):
        # Screen setup
        self.__screen = _turtle.Screen()
        self.__screen.screensize(canvwidth=200, canvheight=200)
        self.__screen.setup(700, 700)
        self.__screen.clear()
        self.__screen.title(window_title)
        self.__screen.bgcolor(background_color)
        self.background_color = background_color

        # Pen setup
        self.__pen = _turtle.Turtle(visible=False)

        # Performance attributes
        self.__pen_width_cache = None
        self.__pen_color_cache = None

    def get_screen_size(self) -> tuple[int, int]:
        """Returns the width and height of the screen."""
        width, height = self.__screen.screensize()
        return width, height

    def draw_line(
        self,
        start_point: _TPoint,
        end_point: _TPoint,
        line_width: int,
        line_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a line from start position to end position.

        Parameters
        ----------
        start_point : tuple[int or float, int or float]
            Position at which the line starts.
        end_point : tuple[int or float, int or float]
            Position at which the line ends.
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
        self.__pen.up()
        self.__pen.speed(__class__.MAX_DRAWING_SPEED)
        self.__pen.goto(start_point)
        # Draw line
        self.__pen.down()
        self.__pen.speed(drawing_speed)
        self.__pen.goto(end_point)

    def draw_dashed_line(
        self,
        start_point: _TPoint,
        end_point: _TPoint,
        total_dashes: int,
        dash_size: int,
        line_width: int,
        line_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a dashed line from start position to end position.

        Parameters
        ----------
        start_point : tuple[int or float, int or float]
            Position at which the line starts.
        end_point : tuple[int or float, int or float]
            Position at which the line ends.
        total_dashes: int
            Positive integer. Number of dashes on the line.
        dash_size : int
            Positive integer.
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

        # Calculate slope
        if start_point == end_point:
            return
        elif start_point[0] == end_point[0]:
            slope = "inf"  # infinite (vertical line)
        elif start_point[1] == end_point[1]:
            slope = 0
        else:
            slope = (end_point[1] - start_point[1]) / (end_point[0] - start_point[0])

        # Calculate line
        if slope != "inf":
            line = lambda t: (t, slope * t + (start_point[1] - start_point[0] * slope))
            t0 = start_point[0]
            dt = (end_point[0] - start_point[0]) / total_dashes
        else:
            line = lambda t: (start_point[0], t)
            t0 = start_point[1]
            dt = (end_point[1] - start_point[1]) / total_dashes

        # Draw dashed line
        for i in range(total_dashes):
            x, y = line(t0 + dt * i)
            if slope != "inf":
                dash_start_point = (
                    x - dash_size,
                    y - dash_size * slope,
                )
                dash_end_point = (
                    x + dash_size,
                    y + dash_size * slope,
                )
            else:
                dash_start_point = (
                    x,
                    y - dash_size,
                )
                dash_end_point = (
                    x,
                    y + dash_size,
                )

            self.__pen.up()
            self.__pen.speed(__class__.MAX_DRAWING_SPEED)
            self.__pen.goto(dash_start_point)
            self.__pen.down()
            self.__pen.speed(drawing_speed)
            self.__pen.goto(dash_end_point)

    def draw_polyline(
        self,
        points: list[_TPoint],
        polyline_width: int,
        polyline_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a polyline by joining the given points.

        Parameters
        ----------
        points : list[tuple[int or float, int or float]]
            Polyline points positions.
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

        # Go to first polyline point without drawing
        self.__pen.speed(__class__.MAX_DRAWING_SPEED)
        self.__pen.up()
        self.__pen.goto(points[0])
        # Draw polyline
        self.__pen.speed(drawing_speed)
        self.__pen.down()
        for point in points[1:]:
            self.__pen.goto(point)

    def draw_arrow(
        self,
        point: _TPoint,
        arrow_size: int,
        arrow_angle: _TNumber,
        arrow_width: int,
        arrow_color: str,
        drawing_speed: int,
    ):
        """Draws an arrow `>` at the given point.

        Parameters
        ----------
        point : tuple[int or float, int or float]
            Point where the arrow will be drawn.
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
        # Draw vector head
        left_arrow = (
            arrow_size * _cos(arrow_angle + _pi * 5 / 4),
            arrow_size * _sin(arrow_angle + _pi * 5 / 4),
        )
        left_arrow_endpoint = (
            point[0] + left_arrow[0],
            point[1] + left_arrow[1],
        )
        self.draw_line(
            point,
            left_arrow_endpoint,
            arrow_width,
            arrow_color,
            drawing_speed,
        )

        right_arrow = (
            arrow_size * _cos(arrow_angle - _pi * 5 / 4),
            arrow_size * _sin(arrow_angle - _pi * 5 / 4),
        )
        right_arrow_endpoint = (
            point[0] + right_arrow[0],
            point[1] + right_arrow[1],
        )

        self.draw_line(
            point,
            right_arrow_endpoint,
            arrow_width,
            arrow_color,
            drawing_speed,
        )

    def draw_text(
        self,
        text: str,
        point: _TPoint,
        text_font: tuple[str, str, str],
        text_color: str,
        align: str,
    ):
        # Pen setup
        if text_color != self.__pen_color_cache:
            self.__pen.color(text_color)
            self.__pen_color_cache = text_color

        # Draw text
        self.__pen.speed(__class__.MAX_DRAWING_SPEED)
        self.__pen.up()
        self.__pen.goto(point)
        self.__pen.write(text, move=False, align=align, font=text_font)

    def clean(self) -> None:
        """Removes all drawings from screen."""
        self.__screen.clear()
        self.__screen.bgcolor(self.background_color)

    def exit_on_click(self):
        """Exits screen when clicked."""
        self.__screen.exitonclick()
