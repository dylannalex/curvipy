[![Downloads](https://pepy.tech/badge/curvipy)](https://pepy.tech/project/curvipy)
![licence](https://img.shields.io/github/license/dylannalex/curvipy?color=blue)

# What is Curvipy?

Curvipy is a Python library for making math animations in a few lines of code.

Curvipy is inspired on manim, an animation engine for making math videos. Despite manim being an exceptionally tool, it is quite hard to learn and use, specially for simple animations. Curvipy solves this issue by providing a less powerful but much easier to use package, with which you can plot two-dimensional curves and vectors.

# Installation

You can start using Curvipy by installing it via pip.

```
$ pip install curvipy
```

# Usage Example

Curvipy is a great tool for learning and teaching math with animations. In this section you can find different topics being explained with Curvipy.

## Functions Translations

A function has been translated when it has been moved in a way that does not change its shape or rotate it in any way. A function can be translated either *vertically*, *horizontally*, or both.

To visualize translations, we will use the function $f(x) = x^{2}$, where $x \in [-15, 15]$.

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

<p align="center">
  <img width="500" height="500" src="docs/source/img/function_x_squared.png">
</p>

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

<p align="center">
  <img width="500" height="500" src="docs/source/img/horizontal_translation.png">
</p>

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

<p align="center">
  <img width="500" height="500" src="docs/source/img/vertical_translation.png">
</p>

## Linear transformations

A linear transformation is a mapping $V \rightarrow W$ between two vector spaces that preserves the operations of vector addition and scalar multiplication.

Curvipy is great for visualizing how a linear transformation transform the two-dimensional space.

### Transformation matrix

In linear algebra, linear transformations can be represented by matrices. If $T$ is a linear transformation mapping $R^n$ to $R^m$ and $\vec{x}$ is a column vector then

$T(\vec{x}) = A\vec{x}$

where $A$ is an $m x n$ matrix called the *transformation matrix* of $T$.

With Curvipy, you can visualize how linear transformations transforms two-dimensional curves with the `curvipy.TransformedCurve` class. Let's visualize how the matrix

$$
A =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

transforms the function $f(x) = sin(x)$.

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

<p align="center">
  <img width="500" height="500" src="docs/source/img/transformation_matrix.png">
</p>

As you can see above, the matrix $A$ rotates the function $f(x)$ 90° anticlockwise.

**Note:**  `curvipy.TransformedCurve`
matrix parameter has the same format as numpy arrays. In fact, you can directly use a numpy array. 

### Matrix multiplication commutative property

For matrix multiplication, the commutative property of multiplication does not hold. This means that, given two matrices $A$ and $B$, generally $AB {\neq} BA$.

To prove this, let's define the matrices

$$
A =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

$$
B = 
\begin{bmatrix}
1 & 1\\
0 & 1
\end{bmatrix}
$$


and see how they transform the curve $f(x) = x^{3}$.

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

<p align="center">
  <img width="500" height="500" src="docs/source/img/mat_multiplication_commutative_property.png">
</p>

As you can see above, transforming $f(x)$ with the matrix $AB$ gives a different result as transforming $f(x)$ with the matrix $BA$.

**Tip:** you can also use numpy arrays to define `AB_transformed_curve` and `BA_transformed_curve` curves, as shown below.

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

You can learn more about Curvipy by visiting the [Documentation Page](https://curvipy.readthedocs.io/en/latest/).
