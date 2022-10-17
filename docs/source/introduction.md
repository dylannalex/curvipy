# What is Curvipy?

Curvipy is a Python library for making math animations in a few lines of code.

Curvipy is inspired on [manim](https://github.com/3b1b/manim), an animation engine for making math videos. Despite manim being an exceptionally tool, it is quite hard to learn and use, specially for simple animations. Curvipy solves this issue by providing a less powerful but much easier to use package, with which you can plot two-dimensional curves and vectors.

# Installation

You can start using Curvipy by installing it via pip.

```{code-block}
$ pip install curvipy
```

```{note} Curvipy requires turtle package. If you don't have it, it will be automatically installed.
```

# Usage Example

Curvipy is a great tool for learning and teaching math with animations. In this section you can find different topics being explained with Curvipy.

## Functions Translations

A function has been translated when it has been moved in a way that does not change its shape or rotate it in any way. A function can be translated either *vertically*, *horizontally*, or both.

To visualize translations, we will use the function {math}`f(x) = x^{2}`, where {math}`x \in [-15, 15]`.

```python
import curvipy
import turtle


def f(x):
    return x**2


plotter = curvipy.Plotter(x_axis_scale=50, y_axis_scale=20)
interval = curvipy.Interval(start=-15, end=15, samples=45)
plotter.plot_curve(curvipy.Function(f), interval)

turtle.exitonclick()
```

![image](img/function_x_squared.png){#imgattr width="500px" align=center}

### Horizontal Translation

In a horizontal translation, the function is moved along the x-axis.

```python
import curvipy
import turtle


def f(x):
    return x**2


def g(x):
    """f(x) moved 3 units to the right."""
    return f(x - 3)


def m(x):
    """f(x) moved 3 units to the left."""
    return f(x + 3)


plotter = curvipy.Plotter(x_axis_scale=50, y_axis_scale=20)
interval = curvipy.Interval(start=-15, end=15, samples=45)
plotter.curve_color = "#FF7B61"  # Red
plotter.plot_curve(curvipy.Function(g), interval)
plotter.curve_color = "#F061FF"  # Purple
plotter.plot_curve(curvipy.Function(m), interval)

turtle.exitonclick()
```

![image](img/horizontal_translation.png){width="500px" align=center}

### Vertical Translation

In a horizontal translation, the function is moved along the y-axis.

```python
import curvipy
import turtle


def f(x):
    return x**2


def g(x):
    """f(x) moved 3 units down."""
    return f(x) - 3


def m(x):
    """f(x) moved 3 units up."""
    return f(x) + 3


plotter = curvipy.Plotter(x_axis_scale=50, y_axis_scale=20)
interval = curvipy.Interval(start=-15, end=15, samples=45)
plotter.curve_color = "#FF7B61"  # Red
plotter.plot_curve(curvipy.Function(g), interval)
plotter.curve_color = "#F061FF"  # Purple
plotter.plot_curve(curvipy.Function(m), interval)

turtle.exitonclick()
```

![image](img/vertical_translation.png){width="500px" align=center}

## Linear transformations

A linear transformation is a mapping {math}`V \rightarrow W` between two vector spaces that preserves the operations of vector addition and scalar multiplication.

Curvipy is great for visualizing how a linear transformation transform the two-dimensional space.

### Transformation matrix

In linear algebra, linear transformations can be represented by matrices. If {math}`T` is a linear transformation mapping {math}`R^n` to {math}`R^m` and {math}`\vec{x}` is a column vector then

{math}`T(\vec{x}) = A\vec{x}`

where {math}`A` is an {math}`m x n` matrix called the *transformation matrix* of {math}`T`.

With Curvipy, you can visualize how linear transformations transforms two-dimensional curves with the `curvipy.TransformedCurve` class. Let's visualize how the matrix

{math}`A = \begin{pmatrix}0 & -1\\1 & 0\end{pmatrix}`

transforms the function {math}`f(x) = sin(x)`.

```python
import math
import curvipy
import turtle


curve = curvipy.Function(math.sin)
interval = curvipy.Interval(-10, 10, 50)
A = ((0, -1), (1, 0))
plotter = curvipy.Plotter(x_axis_scale=25, y_axis_scale=25)

# Plot curve:
plotter.curve_color = "#FF7B61"  # Red
plotter.plot_curve(curve, interval)
# Plot transformed curve:
plotter.curve_color = "#457B9D"  # Blue
plotter.plot_curve(curvipy.TransformedCurve(A, curve), interval)

turtle.exitonclick()  # Exits plotter on click
```

![image](img/transformation_matrix.png){width="500px" align=center}

As you can see above, the matrix {math}`A` rotates the function {math}`f(x)` 90° anticlockwise.

```{note} 
`curvipy.TransformedCurve`
matrix parameter has the same format as numpy arrays. In fact, you can directly use a numpy array. 
```

### Matrix multiplication commutative property

For matrix multiplication, the commutative property of multiplication does not hold. This means that, given two matrices {math}`A` and {math}`B`, generally {math}`AB {\neq} BA`.

To prove this, let's define the matrices

{math}`A = \begin{pmatrix}0 & -1\\1 & 0\end{pmatrix}` and {math}`B = \begin{pmatrix}1 & 1\\0 & 1\end{pmatrix}`

and see how they transform the curve {math}`f(x) = x^{3}`.

```python
import curvipy
import turtle


def f(x):
    return x**3


curve = curvipy.Function(f)
interval = curvipy.Interval(-10, 10, 70)
plotter = curvipy.Plotter(x_axis_scale=25, y_axis_scale=25, curve_width=6)

A = ((0, -1), (1, 0))
B = ((1, 1), (0, 1))

AB_transformed_curve = curvipy.TransformedCurve(A, curvipy.TransformedCurve(B, curve))
BA_transformed_curve = curvipy.TransformedCurve(B, curvipy.TransformedCurve(A, curve))

# Plot f(x) = x^3 in Orange:
plotter.curve_color = "#FFC947"  # Yellow
plotter.plot_curve(curve, interval)

# Plot AB transformed curve in Red:
plotter.curve_color = "#FF7B61"  # Red
plotter.plot_curve(AB_transformed_curve, interval)

# Plot BA transformed curve in Blue:
plotter.curve_color = "#457B9D"  # Blue
plotter.plot_curve(BA_transformed_curve, interval)

turtle.exitonclick()  # Exits plotter on click
```

![image](img/mat_multiplication_commutative_property.png){width="500px" align=center}

As you can see above, transforming {math}`f(x)` with the matrix {math}`AB` gives a different result as transforming {math}`f(x)` with the matrix {math}`BA`.

```{tip}
You can also use numpy arrays to define `AB_transformed_curve` and `BA_transformed_curve` curves, as shown below.
```

```python
import numpy as np
import curvipy


A = np.array(((0, -1), (1, 0)))
B = np.array(((1, 1), (0, 1)))
AB = np.matmul(A, B)
BA = np.matmul(B, A)


AB_transformed_curve = curvipy.TransformedCurve(AB, curve)
BA_transformed_curve = curvipy.TransformedCurve(BA, curve)
```

You can learn more about Curvipy by going through the [Documentation](documentation.md) section or by directly visiting Curvipy on [Github](https://github.com/dylannalex/curvipy) in order to check out the source code itself.