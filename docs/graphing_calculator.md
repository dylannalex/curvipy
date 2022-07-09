## :pencil2: GraphingCalculator

### :pushpin: Attributes

```python
from curvipy import GraphingCalculator


graphing_calculator = GraphingCalculator(
    window_title="curvipy",
    drawing_speed=11,
    background_color="#F1FAEE",
    curve_color="#457B9D",
    curve_width=4,
    vector_color="#E63946",
    vector_width=3,
    vector_head_size=10,
    show_axis=True,
    axis_color="#A8DADC",
    axis_width=2,
)
# The attribute values shown above are the default values 
```

All this are public attributes. You can easily change their value as shown below:

```python
graphing_calculator.attribute_name = attribute_value
```

For example:

```python
graphing_calculator.curve_color = "red"
graphing_calculator.curve_width = 4
graphing_calculator.vector_color = "#FF5A5F"
```

### :pushpin: Methods

#### :round_pushpin: graphing_calculator.draw_curve()

This method draws a given curve.

```python
graphing_calculator.draw_curve(curve, domain_interval, x_axis_scale=10, y_axis_scale=10)
```

- _**curve:**_ curve to draw
- _**domain_interval:**_ curve function domain interval

```python
def f(x):
    return 1/x 

# f(0) is not defined, so 0 cannot be included in our domain_interval.
# valid domain_interval = (1, 10)
# invalid domain_interval = (-10, 10), since 0 is between -10 and 10

graphing_calculator.draw_curve(f, (-10, -1))
graphing_calculator.draw_curve(f, (1, 10))
```

- _**x_axis_scale:**_ integer to scale x axis (default is 10)

```python
def f(x):
    return x ** (1 / 2)


# In this example x must be 0 or greater. However, if we want to draw f(x)
# from x=0 to x=100 (thus domain_interval = (0, 100)) we are going to see
# that f(x) goes off the screen before reaching x=100.
# We can fix that by scaling x axis by a smaller scalar.

graphing_calculator.draw_curve(f, (0, 100), x_axis_scale=3)
```

- _**y_axis_scale:**_  integer to scale y axis (default is 10)

```python
def f(x):
    return x**2 

# In this example we can choose any domain interval, since f(x) is defined
# for all x. However, if we want to draw f(x) from x=-10 to x=10 (thus
# domain_interval = (-10, 10)) we are going to see that f(x) goes off the 
# screen too fast, preventing us from visualizing the function on the 
# specified domain interval.
# We can fix this by scaling y axis by a smaller scalar.

graphing_calculator.draw_curve(f, (-10, 10), y_axis_scale=1)
```

#### :round_pushpin: graphing_calculator.draw_animated_curve()

This method is based on the idea that the graph of a parametrized function **f(t) = [x(t), y(t)]** is nothing but the curve formed by joining all the vectors **[x(t), y(t)]** head. <br>
```graphing_calculator.draw_animated_curve()``` illustrates that by first drawing the set of vectors **{[x(t), y(t)] | t ∈ R}** and then joining their heads.

```python
graphing_calculator.draw_animated_curve(
    parametrized_function, domain_interval, vector_frequency, x_axis_scale, y_axis_scale
)
```

- _**parametrized_function:**_ curves parametrized function
- _**domain_interval:**_ curve function domain interval
- _**vector_frequency:**_ the frequency which vectors will be drawn. The lower frequency the more vectors (default is 2)
- _**x_axis_scale:**_ integer to scale x axis (default is 10)
- _**y_axis_scale:**_  integer to scale y axis (default is 10)

```python
def f(t):
    return t, t + 10

graphing_calculator.draw_animated_curve(f, (-10, 10), vector_frequency=3)
```

```vector_frequency=3``` means that a vector will be drawn every time **t** changes 3 units, starting by **t=-10** (which is the first value of our domain interval). This means that for the values of **t** **{-10, -7, -4, -1, 2, 5, 8}** a vector will be drawn, generating the following set of vectors: **{f(-10), f(-7), f(-4), f(-1), f(2), f(5), f(8)}**. <br>
Setting a negative value for ```vector_frequency``` wont draw any vector.


#### :round_pushpin: graphing_calculator.draw_vector()

This method draws a two-dimensional vector

```python
graphing_calculator.draw_vector(head, tail=(0,0), x_axis_scale=10, y_axis_scale=10)
```

- _**head:**_ vector ending point
- _**tail:**_ vector starting point (default is the origin (0, 0))
- _**x_axis_scale:**_ integer to scale x axis (default is 10)
- _**y_axis_scale:**_  integer to scale y axis (default is 10)

```python
vector = (1, 2)
graphing_calculator.draw_vector(vector, x_axis_scale=10, y_axis_scale=10)
```

#### :round_pushpin: graphing_calculator.clear()

This method clears the graphic calculator screen. Changes made to ```background_color```, ```show_axis```, ```axis_color``` and ```axis_width``` will be applied after calling this method.