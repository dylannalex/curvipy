# Graph Plotter

## Plotter

```{eval-rst}
.. autoclass:: curvipy.Plotter
    :members:
```

## Screen Configuration

```{eval-rst}
.. autoclass:: curvipy.ScreenConfiguration
    :members:
```

## Plotting Configuration

```{eval-rst}
.. autoclass:: curvipy.PlottingConfiguration
    :members:
```

## Axes Configuration

```{eval-rst}
.. autoclass:: curvipy.AxesConfiguration
    :members:
```

# Curves

With Curvipy you can plot two-dimensional curves. In this section you can find classes provided by Curvipy for defining curves.

## Curve

```{eval-rst}
.. autoclass:: curvipy.Curve
    :members:
```

**Example:**
```python
import math

class Sin(Curve):
    def __init__(self, amplitude, frequency):
        self.interval = curvipy.Interval(-2 * math.pi, 2 * math.pi, 100)
        self.function = lambda x: amplitude * math.sin(x * frequency)
    
    def points(self):
        return [(x, self.function(x)) for x in self.interval]
```

You can define your own [Curve](curvipy.Curve) class or use on the classes provided by Curvipy shown below.

## Interval

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

## Function

```{eval-rst}
.. autoclass:: curvipy.Function
    :members:
```

**Example:**

```python
import math
import curvipy

interval = curvipy.Interval(-2 * math.pi, 2 * math.pi, 200)
curve = curvipy.Function(math.sin, interval)
```

## Parametric Function

```{eval-rst}
.. autoclass:: curvipy.ParametricFunction
    :members:
```

**Example:**

```python
import curvipy

interval = curvipy.Interval(-5, 5, 200)
parametric_function = lambda t: (t, t**2)
curve = curvipy.ParametricFunction(parametric_function, interval)
```

## Transformed Curve

```{eval-rst}
.. autoclass:: curvipy.TransformedCurve
    :members:
```

**How it works:**

Given a linear transformation {math}`T` with its respective transformation matrix {math}`M_{2 \times 2}` and a set of points {math}`P` from a curve {math}`C`, [TransformedCurve.points()](curvipy.TransformedCurve.points()) computes the set of points

```{math}
P_T = \{M_{2 \times 2} \times p_i \mid p_i \in P\}
```

which defines the transformed curve {math}`T(C)`.

**Example:**

```python
import math
import curvipy

interval = curvipy.Interval(-2 * math.pi, 2 * math.pi, 200)
curve = curvipy.Function(math.sin, interval)
rotation_matrix = ((0, 1), (-1, 0))  # 90° anticlockwise rotation
rotated_curve = curvipy.TransformedCurve(curve, rotation_matrix)  # Rotated sin(x)
```

# Vectors

```{eval-rst}
.. autoclass:: curvipy.Vector
    :member-order: bysource
    :members:
    :special-members: __getitem__,__mul__,__add__,__sub__,__eq__
```
