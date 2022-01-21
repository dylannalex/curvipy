from typing import Callable, Union
import turtle


class GraphingCalculator(turtle.Turtle):
    def __init__(
        self,
        background_color: Union[tuple[int, int, int], str] = "white",
        function_color: Union[tuple[int, int, int], str] = "black",
        function_width: int = 3,
        show_axis: bool = True,
        axis_color: Union[tuple[int, int, int], str] = "grey",
        axis_width: int = 2,
    ) -> None:
        turtle.Turtle.__init__(self)
        self.shapesize(0.1, 0.1, 0.1)
        self.shape("square")
        self.speed("fastest")
        turtle.bgcolor(background_color)

        # Function attributes:
        self.function_color = function_color
        self.function_width = function_width

        # Axis attributes
        self.axis_color = axis_color
        self.show_axis = show_axis
        self.axis_width = axis_width

        if self.show_axis:
            self._draw_axis()
        else:
            self.width(function_width)
            self.color(function_color)

    def draw(
        self,
        curve: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        """
        Defines if a given curve is a function or a parametrized curve and
        draws it.
        """
        curve_image = curve(domain_interval[0])
        if len(curve_image) == 1:
            self.draw_function(curve, domain_interval, x_axis_scale, y_axis_scale)
        elif len(curve_image) == 2:
            self.draw_parametrized_curve(
                curve, domain_interval, x_axis_scale, y_axis_scale
            )
        else:
            raise ValueError("'curve' should be a function or parametrized curve")

    def draw_function(
        self,
        f: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        """
        f(Callable):                        function to draw
        domain_interval(tuple[int, int]):   x interval where the function is going to be drawn
        x_axis_scale(int):                  x axis scaling factor
        y_axis_scale(int):                  y axis scaling factor
        """
        for x in range(domain_interval[0], domain_interval[1] + 1, 1):
            f_point = (
                x_axis_scale * x,
                y_axis_scale * f(x),
            )
            if x == domain_interval[0]:
                self._goto_without_drawing(f_point)
            else:
                self.goto(f_point)

    def draw_parametrized_curve(
        self,
        parametrized_curve: Callable,
        domain_interval: tuple[int, int],
        x_axis_scale: int = 10,
        y_axis_scale: int = 10,
    ) -> None:
        """
        parametrized_curve(Callable):       curve to draw
        domain_interval(tuple[int, int]):   t interval where the curve is going to be drawn
        x_axis_scale(int):                  x axis scaling factor
        y_axis_scale(int):                  y axis scaling factor
        """
        for t in range(domain_interval[0], domain_interval[1] + 1, 1):
            f_vector = parametrized_curve(t)
            scaled_f_vector = (
                x_axis_scale * f_vector[0],
                y_axis_scale * f_vector[1],
            )
            if t == domain_interval[0]:
                self._goto_without_drawing(scaled_f_vector)
            else:
                self.goto(scaled_f_vector)

    def _goto_without_drawing(self, position: tuple[int, int, int]) -> None:
        self.up()
        self.goto(position)
        self.down()

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

        self.color(self.function_color)

        self.width(self.function_width)
        self.color(self.function_color)

    def clear(self) -> None:
        turtle.clearscreen()
        if self.show_axis:
            self._draw_axis()