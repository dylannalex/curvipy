## :pencil2: GraphingCalculator

### :pushpin: Attributes
```
from curvipy import GraphingCalculator


graphing_calculator = GraphingCalculator(
    background_color="white",
    curve_color="black",
    curve_width=3,
    show_axis=True,
    axis_color="grey",
    axis_width=2,
)
```

- _**background_color:**_ color name or hex code
- _**curve_color:**_ color name or hex code
- _**curve_width:**_ integer value
- _**show_axis:**_ boolean value
- _**axis_color:**_ color name or hex code
- _**axis_width:**_ integer value


All this are public attributes. You can easily change their value as shown below:
```
graphing_calculator.attribute_name = attribute_value
```
For example:
```
graphing_calculator.curve_color = "red"
graphing_calculator.curve_width = 4
```

### :pushpin: Methods

#### :round_pushpin: graphing_calculator.draw():

This method draws the given curve.

```
graphing_calculator.draw(curve, domain_interval, x_axis_scale=10, y_axis_scale=10)
```
- _**curve:**_ curve to be drawn
- _**domain_interval:**_ curve function domain interval. See example below
```
def f(x):
    return 1/x 

# f(0) is not defined, so 0 cannot be included in our domain_interval.
# valid domain_interval = (1, 10)
# invalid domain_interval = (-10, 10), since 0 is between -10 and 10

graphing_calculator.draw(f, (-10, -1))
graphing_calculator.draw(f, (1, 10))
```
- _**x_axis_scale:**_ integer to scale x axis (default is 10). See example below
```
def f(x):
    return x ** (1 / 2)


# In this example x must be 0 or greater. However, if we want to draw f(x)
# from x=0 to x=100 (thus domain_interval = (0, 100)) we are going to see
# that f(x) goes off the screen before reaching x=100.
# We can fix that by scaling x axis by a smaller scalar.

graphing_calculator.draw(f, (0, 100), x_axis_scale=3)
```
- _**y_axis_scale:**_  integer to scale y axis (default is 10). See example below
```
def f(x):
    return x**2 

# In this example we can choose any domain interval, since f(x) is defined
# for all x. However, if we want to draw f(x) from x=-10 to x=10 (thus
# domain_interval = (-10, 10)) we are going to see that f(x) goes off the 
# screen too fast, preventing us from visualizing the function on the 
# specified domain interval.
# We can fix this by scaling y axis by a smaller scalar.

graphing_calculator.draw(f, (-10, 10), y_axis_scale=1)
```

#### :round_pushpin: graphing_calculator.clear():

This method clears the graphic calculator screen. Changes made to ```background_color```, ```show_axis```, ```axis_color``` and ```axis_width``` will be applied after calling this method.