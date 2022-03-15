## :pencil2: Linear Transformations

**curvipy** provides a ```lintrans``` module which contains functions for modifying curves with linear transformations.

```python
from curvipy import lintrans
```

### :pushpin: Applying linear transformations to curves

A parametrized function ```f(t) = <x(t), y(t)>``` image is the set of vectors ```{<x(t), y(t)> | t ∈ R}```. ```f(t)``` graph is nothing but the curve formed by joining all the vectors head, in other words, ```f(t)``` graph is the set of points ```{P(x(t), y(t)) | t ∈ R}```.<br>

Applying linear transformations to curves is based on the idea that applying a linear transformation ```T``` to ```f(t)``` can be thought as applying ```T``` to each vector in ```{<x(t), y(t)> | t ∈ R}```. This means that ```T(f(t))``` image is ```{T(<x(t), y(t)>) | t ∈ R}``` and its graph is the curve formed by joining the vectors head in that set.

_**NOTE:**_ because of the explained above, this module only works with curves defined as parametrized functions.


### :pushpin: lintrans.rotate_curve()

Rotates a curve anticlockwise by the given angle.<br/>

**Parameters:**

```python
lintrans.rotate_curve(curve, angle)
```

- _**curve:**_ parametrized function 
- _**angle:**_ angle in radians

**Example:**

```python
def square_root(t):
    return t, t ** (1 / 2)

angle = pi / 4  # 90 degrees
rotated_square_root = lintrans.rotate_curve(square_root, angle)
graphing_calculator.draw(rotated_square_root, (0, 25))
```

### :pushpin: lintrans.scale_curve()

Scales the given curve by the given scalar.<br/>

**Parameters:**

```python
lintrans.scale_curve(curve, scalar)
```

- _**curve:**_ parametrized function 
- _**scalar:**_ scalar for scaling the curve

**Example:**

```python
def square_root(t):
    return t, t ** (1 / 2)

scalar = 2  # The function is going to be twice as bigger
scaled_square_root = lintrans.scale_curve(square_root, 2)
graphing_calculator.draw(scaled_square_root, (0, 25))
```

### :pushpin: lintrans.transform_curve()

This function lets you apply any linear transformation to a curve. 

**Parameters:**

```python
lintrans.transform_curve(curve, transformation_matrix)
```

- _**curve:**_ parametrized function
- _**transformation_matrix:**_ linear transformation

**Example:**

```python
# Imagine we want to define the following transformation matrix:
#
# transformation_matrix = [ 1   2 ]
#                         [ 3   4 ]
#
# We can do so with Python lists (or tuples):

transformation_matrix = [[1, 2], [3, 4]]

# Or we can use numpy arrays (which might be more useful):

import numpy as np
transformation_matrix = np.array(((1, 2), (3, 4)))

# Let's transform the square root function

def square_root(t):
    return t, t ** (1 / 2)

transformed_square_root = lintrans.transform_curve(square_root, transformation_matrix)
graphing_calculator.draw(transformed_square_root, (0, 25))
```
