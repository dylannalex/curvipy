## :pencil2: Introduction


### :pushpin: Getting started
To start drawing curves you need to create a ```GraphingCalculator``` object:

```
from curvipy import GraphingCalculator

graphing_calculator = GraphingCalculator()
```

The next step is to define the curve you want to draw. In **curvipy** this can be done by:

- Defining the curve as a function ```y = f(x)```: 
```
def square_root(x):
    return x ** (1 / 2)

graphing_calculator.draw_curve(square_root, (0, 25))  # We want to draw the function from x = 0 to x = 25
```

- Defining the curve as a parametrized function ```f(t) = <x(t), y(t)>```: 
```
def square_root(t):
    return t, t ** (1 / 2)

graphing_calculator.draw_curve(square_root, (0, 25))  # We want to draw the curve from t = 0 to t = 25
```

Check out [graphing_calculator.md](./graphing_calculator.md) to see all ```GraphingCalculator``` attributes and methods.


### :pushpin: Linear transformations

**curvipy** provides a ```lintrans``` module which contains functions to apply linear transformations to curves.
Check out [lintrans.md](./lintrans.md) to see you can do with ```curvipy.lintrans``` module.