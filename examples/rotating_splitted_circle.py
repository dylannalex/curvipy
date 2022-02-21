from curvipy import GraphingCalculator
from curvipy import lintrans
from turtle import exitonclick
from time import sleep
import math


def t_prime(t, radius):
    if t < 0:
        return t + radius
    else:
        return t - radius


def splitted_circle(t, radius):
    if t < 0:
        return t, math.sqrt(radius ** 2 - t_prime(t, radius) ** 2)
    else:
        return t, -math.sqrt(radius ** 2 - t_prime(t, radius) ** 2)


def draw_rotated_circle(graphing_calculator: GraphingCalculator, radius, angle):
    rotated_circle = lintrans.rotate_curve(lambda t: splitted_circle(t, radius), angle)
    graphing_calculator.draw_animated_curve(
        rotated_circle, (-2 * radius, 2 * radius), vector_frequency=3
    )


def main():
    graphing_calculator = GraphingCalculator(
        background_color="black",
        curve_color="#FF5A5F",
        curve_width=4,
        vector_color="#00A61C",
        vector_width=3,
        vector_head_size=10,
        show_axis=True,
        axis_color="grey",
        axis_width=2,
    )

    radius = 17
    max_angle = 50
    angle_variation = 10
    for angle in range(0, max_angle, angle_variation):
        angle_rad = angle * 2 * math.pi / 360
        draw_rotated_circle(graphing_calculator, radius, angle_rad)
        sleep(0.5)
        graphing_calculator.clear()


if __name__ == "__main__":
    main()
    exitonclick()
