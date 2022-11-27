import turtle as _turtle


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
        start_point: tuple[int or float, int or float],
        end_point: tuple[int or float, int or float],
        line_width: int,
        line_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a line from start position to end position.

        Parameters
        ----------
        start_point : int
            Position at which the line starts.
        end_point : int
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

    def draw_polyline(
        self,
        points: list[tuple[int, int]],
        polyline_width: int,
        polyline_color: str,
        drawing_speed: int,
    ) -> None:
        """Draws a polyline by joining the given points.

        Parameters
        ----------
        points : list[tuple[int, int]]
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

    def clean(self) -> None:
        """Removes all drawings from screen."""
        self.__screen.clear()
        self.__screen.bgcolor(self.background_color)

    def exit_on_click(self):
        """Exits screen when clicked."""
        self.__screen.exitonclick()
