# pydrawer :triangular_ruler:	

![licence](https://img.shields.io/github/license/dylannalex/pydrawer?color=blue)

The Python package for visualizing curves and linear transformations in a super simple way.

## :pencil2: Installation

Install pydrawer package with pip:
```
$ pip install pydrawer
```
or clone the repository:
```
$ git clone https://github.com/dylannalex/pydrawer.git
```

## :pencil2: Usage

### :pushpin: Drawing curves
To start drawing curves you need to create a ```GraphingCalculator``` object:

```
from pydrawer import GraphingCalculator

graphing_calculator = GraphingCalculator()
```

**pydrawer** let you draw parametrized curves and mathematical functions. Lets create and draw
the square root of x function for this example:

```
def square_root(x):
    return x ** (1 / 2)

graphing_calculator.draw(square_root, (0, 25))  # We want to draw the function from x = 0 to x = 25
```

You can also accomplish the same result by defining the square root of x as a parameterized function:

```
def square_root(t):
    return t, t ** (1 / 2)

graphing_calculator.draw(square_root, (0, 25))  # We want to draw the curve from t = 0 to t = 25
```

### :pushpin: Linear transformations

**pydrawer** provides a ```curves``` module which contains functions for modifying curves with linear
transformations.
```
from pydrawer import curves
```

#### :round_pushpin: ```curves.transform_curve()```
This function let you apply a linear transformation (specified as a matrix) to a parametrized
curve. ```curves.transform_curve()``` returns the transformed curve.<br/><br/>
**Parameters:**
- curve: parametrized curve
- matrix: linear transformation's matrix

The matrix is a tuple of tuples (or list of lists) which has the same structure as numpy arrays. A matrix 
<br/>[ a   b ]<br/>[ c   d ]<br/>
should be defined as:
```
matrix = ((a,b), (c,d))
```
**Example:**
```
matrix = ((1, 0), (0, -2))
graphing_calculator.draw(curves.transform_curve(square_root, matrix), (0, 25))
```

#### :round_pushpin: ```curves.rotate_curve()```
Rotates a curve anticlockwise by the given angle.<br/><br/>
**Parameters:**
- curve: parametrized curve
- angle: angle in radians
<br/>**Example:**
```
angle = pi / 4  # 90 degrees
graphing_calculator.draw(curves.rotate_curve(square_root, angle), (0, 25))
```
#### :round_pushpin: ```curves.scale_curve()```
Scales the given curve by the given scalar.<br/><br/>
**Parameters:**
- curve: parametrized curve
- scalar: scalar for scaling the curve
<br/>**Example:**
```
scalar = 2  # The function is going to be twice as bigger
graphing_calculator.draw(curves.scale_curve(square_root, 2), (0, 25))
```
