# Graph Plotter

Curvipy provides the `Plotter` class.

```{eval-rst}
.. autoclass:: curvipy.Plotter
    :members:
```

# Curves

With Curvipy you can plot two-dimensional curves. In this section you can find classes provided by Curvipy for defining curves.

## Interval class

```{eval-rst}
.. autoclass:: curvipy.Interval
    :members:
```

**Example:**
Suppose we want to plot the function √x with 20 samples.

```python
import curvipy

valid_interval = curvipy.Interval(start=0, end=10, samples=20) 
# All numbers from start to end belong to √x domain.
invalid_interval = curvipy.Interval(start=-10, end=0, samples=20) 
# Negative numbers don't belong to √x domain.
```

## Curve class

```{eval-rst}
.. autoclass:: curvipy.Curve
    :members:
```

You can define your own `Curve` class or use on the classes provided by Curvipy shown below.

## Function class

```{eval-rst}
.. autoclass:: curvipy.Function
    :members:
```

**Example:**

```python
import math
import curvipy

curve = curvipy.Function(math.sin)
```

## ParametricFunction class

```{eval-rst}
.. autoclass:: curvipy.ParametricFunction
    :members:
```

**Example:**

```python
import curvipy

parametric_function = lambda t: (t, t**2)
curve = curvipy.ParametricFunction(parametric_function)
```

## TransformedCurve class

```{eval-rst}
.. autoclass:: curvipy.TransformedCurve
    :members:
```

**Example:**

```python
import math
import curvipy

curve = curvipy.Function(math.sin)
rotation_matrix = ((0, 1), (-1, 0))  # 90° anticlockwise rotation
rotated_curve = curvipy.TransformedCurve(curve, rotation_matrix)  # Rotated sin(x)
```

# Vectors

Vectors can be defined with the `Vector` class.

```{eval-rst}
.. autoclass:: curvipy.Vector
    :members:
```
