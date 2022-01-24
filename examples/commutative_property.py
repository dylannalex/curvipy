import numpy as np
from curvipy import GraphingCalculator
from curvipy import curves
from time import sleep

"""
This example uses the numpy library. If you don't have it already you can simply
install it with pip:
$ pip install numpy


In this example we are going to see how not all matrices multiplication are
commutative. For doing it we are going to define two matrices:

                    A = [ 0  1 ]        B = [ 1  1 ] 
                        [-1  0 ]            [ 0  1 ] 

- A rotates vectors 90° anticlockwise
- B is a shear matrix (https://en.wikipedia.org/wiki/Shear_matrix)

To visualize how matrix multiplication works, we are going to use the curve
f(t) = <t, t> (the y = x function). 
We can think of f(t) as the curve formed by joining all the <t, t> vectors' head.
Applying a matrix to f(t) means that we are applying a linear transformation to
each vector and then joining their heads again.

Lets see if applying the AB matrix to f(t) gives the same transformed curve as
if we apply the BA matrix!
"""


def f(t):
    """
    This curve represents the y=x function
    """
    return t, t


A = np.array(((0, 1), (-1, 0)))
B = np.array(((1, 1), (0, 1)))

AB = np.matmul(A, B)
BA = np.matmul(B, A)


calc = GraphingCalculator(
    background_color="black", curve_color="#2CFF2C", curve_width=9
)

print("Drawing original curve")
calc.draw(f, (-20, 20))
sleep(2)
calc.clear()

print("Drawing curve transformed by matrix AB")
calc.draw(curves.transform_curve(f, AB), (-20, 20))
sleep(2)
calc.clear()

print("Drawing curve transformed by matrix BA")
BA = np.matmul(B, A)
calc.draw(curves.transform_curve(f, BA), (-20, 20))
sleep(2)
