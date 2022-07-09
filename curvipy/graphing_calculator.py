from typing import Any, Callable
from math import sqrt, sin, acos, cos, pi
import turtle


def _is_int(result: Any) -> bool:
    try:
        int(result)
        return True
    except Exception:
        return False


def _is_float(result: Any) -> bool:
    try:
        float(result)
        return True
    except Exception:
        return False


class GraphingCalculator(turtle.Turtle):
    def __init__(
        self,
        window_title: str = "curvipy",
        drawing_speed: int = 11,
        background_color: str = "#F1FAEE",
        curve_color: str = "#457B9D",
        curve_width: int = 4,
        vector_color: str = "#E63946",
        vector_width: int = 3,
        vector_head_size: int = 10,
        show_axis: bool = True,
        axis_color: str = "#A8DADC",
        axis_width: int = 2,
    ) -> None:
        """
        :param window_title: title to display on window
        :param drawing_speed: integer value
        :param background_color: color name or hex code
        :param curve_color: color name or hex code
        :param curve_width: integer value that specifies curve width
        :param show_axis: draws axis if true
        :param axis_color: color name or hex code
        :param axis_width: axis value that specifies curve width
        """

        turtle.Turtle.__init__(self)
        self.shapesize(0.1, 0.1, 0.1)
        self.shape("square")
        turtle.title(window_title)
        turtle.bgcolor(background_color)

        # Screen attributes
        self.drawing_speed = drawing_speed
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

        if self.show_axis:
            self._draw_axis()

    def draw_vector(
        self,
        head: tuple[float, float],
        tail: tuple[float, float] = (0, 0),
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:

        vector_coordinates = (head[0] - tail[0], head[1] - tail[1])

        # Check if vector is the cero vector (v = [0, 0])
        vector_norm = sqrt(vector_coordinates[0] ** 2 + vector_coordinates[1] ** 2)
        if vector_norm == 0:
            return

        # Graphing calculator setup
        self.color(self.vector_color)
        self.width(self.vector_width)

        # Draw vector
        scaled_tail = (tail[0] * x_axis_scale, tail[1] * y_axis_scale)
        self._goto_without_drawing(scaled_tail)
        scaled_head = (head[0] * x_axis_scale, head[1] * y_axis_scale)
        self._goto_drawing(scaled_head)

        # Draw vector head
        vector_angle = acos(vector_coordinates[0] / vector_norm)

        if vector_coordinates[1] < 0:
            vector_angle *= -1

        left_head_vector = (
            self.vector_head_size * cos(vector_angle + pi * 5 / 4),
            self.vector_head_size * sin(vector_angle + pi * 5 / 4),
        )
        left_head_endpoint = (
            scaled_head[0] + left_head_vector[0],
            scaled_head[1] + left_head_vector[1],
        )

        self._goto_drawing(left_head_endpoint)

        right_head_vector = (
            self.vector_head_size * cos(vector_angle - pi * 5 / 4),
            self.vector_head_size * sin(vector_angle - pi * 5 / 4),
        )
        right_head_endpoint = (
            scaled_head[0] + right_head_vector[0],
            scaled_head[1] + right_head_vector[1],
        )

        self._goto_without_drawing(scaled_head)
        self._goto_drawing(right_head_endpoint)

    def draw_curve(
        self,
        curve: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        """
        Determines if a given curve is a function or a parametrized curve and
        draws it.

        :param curve: parametrized curve or function to draw
        :param domain_interval: curve domain interval
        :param x_axis_scale: x axis scaling factor
        :param y_axis_scale: y axis scaling factor
        """
        curve_evaluation = curve(domain_interval[0])
        if _is_int(curve_evaluation) or _is_float(curve_evaluation):
            self._draw_function(curve, domain_interval, x_axis_scale, y_axis_scale)
        elif len(curve_evaluation) == 2:
            self._draw_parametrized_function(
                curve, domain_interval, x_axis_scale, y_axis_scale
            )
        else:
            raise ValueError("'curve' should be a function or parametrized curve")

    def draw_animated_curve(
        self,
        parametrized_function: Callable,
        domain_interval: tuple[int, int],
        vector_frequency: int = 2,
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        """
        Given a parametrized function f(t) = [x(t), y(t)], draws a the
        set of vectors {[x(t), y(t)] | t e domain_interval} and then
        draws f(t) graph.

        :param parametrized_function: curve to draw
        :param domain_interval: curve domain interval
        :param vector_frequency: the frequency which vectors will be
        drawn. The lower frequency the more vectors
        :param x_axis_scale: x axis scaling factor
        :param y_axis_scale: y axis scaling factor
        """
        for t in range(domain_interval[0], domain_interval[1] + 1, vector_frequency):
            f_vector = parametrized_function(t)
            self.draw_vector(f_vector, (0, 0), x_axis_scale, y_axis_scale)
        self._draw_parametrized_function(
            parametrized_function, domain_interval, x_axis_scale, y_axis_scale
        )

    def _draw_function(
        self,
        f: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        self.color(self.curve_color)
        self.width(self.curve_width)
        for x in range(domain_interval[0], domain_interval[1] + 1, 1):
            f_point = (
                x_axis_scale * x,
                y_axis_scale * f(x),
            )
            if x == domain_interval[0]:
                self._goto_without_drawing(f_point)
            else:
                self._goto_drawing(f_point)

    def _draw_parametrized_function(
        self,
        parametrized_function: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        self.color(self.curve_color)
        self.width(self.curve_width)
        for t in range(domain_interval[0], domain_interval[1] + 1, 1):
            f_vector = parametrized_function(t)
            scaled_f_vector = (
                x_axis_scale * f_vector[0],
                y_axis_scale * f_vector[1],
            )
            if t == domain_interval[0]:
                self._goto_without_drawing(scaled_f_vector)
            else:
                self._goto_drawing(scaled_f_vector)

    def _goto_without_drawing(self, position: tuple[int, int]) -> None:
        self.speed("fastest")
        self.up()
        self.goto(position)
        self.down()

    def _goto_drawing(self, position: tuple[int, int]) -> None:
        self.speed(self.drawing_speed)
        self.down()
        self.goto(position)

    def _draw_axis(self) -> None:
        self.width(self.axis_width)
        self.color(self.axis_color)

        w, h = turtle.screensize()

        # y axis
        self._goto_without_drawing((0, -h * 2))
        self.goto(0, h * 2)

        # x axis
        self._goto_without_drawing((-w * 2, 0))
        self.goto((w * 2, 0))

    def clear(self) -> None:
        """
        Clears the graphic calculator screen.
        """
        turtle.clearscreen()
        turtle.bgcolor(self.background_color)
        if self.show_axis:
            self._draw_axis()
