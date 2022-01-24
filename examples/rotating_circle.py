from curvipy import GraphingCalculator
from curvipy import curves
from turtle import exitonclick
from time import sleep
import math


COLORS = ("#FF5A5F", "#AD5AFF", "#5A91FF", "#5AFF80", "#EAFF5A", "#FF7F47")


def upper_semi_circle(t, radius):
    return t, math.sqrt(radius ** 2 - t ** 2)


def lower_semi_circle(t, radius):
    return t, -math.sqrt(radius ** 2 - t ** 2)


def draw_rotated_circle(calc: GraphingCalculator, radius, angle):
    rotated_upper_semi_circle = curves.rotate_curve(
        lambda t: upper_semi_circle(t, radius), angle
    )
    rotated_lower_semi_circle = curves.rotate_curve(
        lambda t: lower_semi_circle(t, radius), angle
    )

    calc.draw(rotated_upper_semi_circle, (-radius, radius))
    calc.draw(rotated_lower_semi_circle, (-radius, radius))


def main():
    calc = GraphingCalculator(
        background_color="black", curve_color=COLORS[-1], curve_width=5
    )
    radius = 15
    counter = 1
    for angle in range(0, 50, 5):
        draw_rotated_circle(calc, radius, angle * 2 * math.pi / 360)
        calc.curve_color = COLORS[counter % len(COLORS)]
        sleep(0.5)
        calc.clear()
        counter += 1


if __name__ == "__main__":
    main()
    exitonclick()
