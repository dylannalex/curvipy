from curvipy import GraphingCalculator
from curvipy import curves
from turtle import exitonclick
from time import sleep
import math


COLORS = ("#8A9CF2", "#FFB5F3", "#77FF93", "#FFE476")


def semi_circle(t, radius):
    return t, math.sqrt(radius ** 2 - t ** 2)


def draw_circle(calc: GraphingCalculator, radius, angle):
    upper_semi_circle = curves.rotate_curve(lambda t: semi_circle(t, radius), angle)
    lower_semi_circle = curves.rotate_curve(
        lambda t: semi_circle(t, radius), angle + math.pi
    )
    calc.draw(upper_semi_circle, (-radius, radius))
    calc.draw(lower_semi_circle, (-radius, radius))


def main():
    calc = GraphingCalculator(
        background_color="black", curve_color=COLORS[-1], curve_width=5
    )
    radius = 15
    counter = 1
    for angle in range(0, 180, 5):
        draw_circle(calc, radius, angle * 2 * math.pi / 360)
        calc.curve_color = COLORS[counter % len(COLORS)]
        counter += 1
        sleep(0.5)
        calc.clear()


if __name__ == "__main__":
    main()
    exitonclick()
