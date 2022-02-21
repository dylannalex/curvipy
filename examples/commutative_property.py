import numpy as np
from curvipy import GraphingCalculator, graphing_calculator
from curvipy import lintrans


# In this example we are going to use curvipy to prove that not all matrix
# multiplication is commutative.

"""
To visualize how matrix multiplication works, we are going to use the curve
f(t) = <t, t> (which is the function y=x+10 parametrized).

As explained on lintrans.md (https://github.com/dylannalex/curvipy/blob/master/docs/lintrans.md)
we can think of f(t) graph as the curve formed by drawing all the f(t) image
vectors, and then joining their heads.
"""

graphing_calculator = GraphingCalculator(
    background_color="black",
    curve_color="#FF5A5F",
    curve_width=10,
    vector_color="#00A61C",
    vector_width=3,
    vector_head_size=10,
    show_axis=True,
    axis_color="grey",
    axis_width=2,
)


def f(t):
    """
    This curve represents the y=x+10 function
    """
    return t - 10, t


graphing_calculator.draw_animated_curve(f, (-20, 30))
input("Press Enter to continue...")
graphing_calculator.clear()

"""
For doing this let's define two matrices:

                    A = [ 0  1 ]        B = [ 1  1 ] 
                        [-1  0 ]            [ 0  1 ] 

- A rotates vectors 90° anticlockwise
- B is a shear matrix (https://en.wikipedia.org/wiki/Shear_matrix)

If AB = BA, transforming f(t) by AB would generate the same function
as transforming f(t) by BA.

NOTE: keep in mind that applying linear transformations to parametrized
functions means applying the linear transformation to each vector of the
parametrized function. Again, check out lintrans.md for more info.
"""

A = np.array(((0, 1), (-1, 0)))
B = np.array(((1, 1), (0, 1)))

AB = np.matmul(A, B)
BA = np.matmul(B, A)


print("Drawing curve transformed by matrix AB")
graphing_calculator.draw_animated_curve(lintrans.transform_curve(f, AB), (-20, 30))
input("Press Enter to continue...")
graphing_calculator.clear()


print("Drawing curve transformed by matrix BA")
graphing_calculator.draw_animated_curve(lintrans.transform_curve(f, BA), (-20, 30))
input("Press Enter to continue...")

"""
As you could see, f(t) transformed by AB is different from f(t) transformed
by BA. This means we find a counterexample for AB = BA.
"""
