# Contributing to Curvipy
We welcome contributions to Curvipy! Whether you are a seasoned developer or just getting started, there are many ways to get involved.

## Non-Code Contributions
There are many ways to contribute to Curvipy without writing any code:

- _**Share Curvipy with others:**_ Share the library with your friends, colleagues, and online communities. The more people that know about Curvipy, the more likely it is to grow and improve. Additionally, you can contribute to Curvipy by using it to explain math topics on blogs, YouTube, and other platforms. This helps to reach a wider audience and increases the visibility of the library.
- _**Improve documentation:**_ Curvipy's documentation is always in need of improvement. If you see any typos, errors, or areas that could be clearer, feel free to open a pull request or issue to suggest improvements.
- _**Suggest new features:**_ Do you have an idea for a new feature that would make Curvipy even better? We welcome feature proposals! Simply open an issue with your idea and we'll discuss it.

## Code Contributions
If you are interested in contributing code to Curvipy, here are a few things to keep in mind:

- _**Code formatting:**_ Curvipy uses Black for code formatting. Please run Black on your code before submitting a pull request to ensure that it meets the project's formatting standards.
- _**Open an issue:**_ Before making a pull request, we recommend opening an issue to discuss your proposed changes. This helps to ensure that your pull request is focused and addresses a specific problem or need.
- _**Commit messages:**_ When committing your changes, please use clear and concise commit messages that starts with a verb in the present tense. For example: "Add new feature" or "Fix bug".
- _**Pull request template:**_ When creating a pull request, please include a clear and concise description of the changes you are proposing. Be sure to follow the [pull request template](https://github.com/dylannalex/curvipy/blob/main/pull_request_template.md) provided by the project.

We appreciate any and all contributions to Curvipy! Thank you for your interest in helping to improve the library❤️

# Notes for developers

## How Plotter works

### Coordinates system

[curvipy.Plotter](curvipy.Plotter) works with a virtual set of coordinates defined by the a logical width and height. The logical screen size is independent of the real window size, and virtual coordinates are translated to real window coordinates. Despite setting a logical width and height do not affect the window size, it defines the xy-plane coordinate system. This is useful for precisely calibrating the distance between the axes ticks.

If we want the x-axis to have {math}`n \in \mathbb{N}` total ticks with a distance {math}`\Delta x \in \mathbb{R}` between their self, that is

```{math}
\text{x-axis ticks} = \{ \Delta x \cdot i \mid i \in \mathbb{N} \land -\frac{n}{2} \leq i \leq \frac{n}{2} \}
```                                     

and the y-axis to have {math}`m \in \mathbb{N}` total ticks with a distance {math}`\Delta y \in \mathbb{R}` between their self, that is

```{math}
\text{y-axis ticks} = \{ \Delta y \cdot j \mid j \in \mathbb{N} \land -\frac{m}{2} \leq j \leq \frac{m}{2} \}
```    

then
```{math}
\text{logical width} = n \cdot \Delta x

\text{logical height} = m \cdot \Delta y
```

Note that _the x-axis length equals the logical width and the y-axis length equals the logical height_.

### Plotting mechanic

For plotting curves and vectors, [curvipy.Plotter](curvipy.Plotter) uses the [ScreenFacade](curvipy._screen.ScreenFacade) class for drawing lines, polylines and arrows on screen.

```{eval-rst}
.. autoclass:: curvipy._screen.ScreenFacade
    :members:
    :member-order: bysource
```

**Note:** [ScreenFacade](curvipy._screen.ScreenFacade) is a composite of [curvipy.Plotter](curvipy.Plotter), therefore users should not access this class (that is why you will not find [ScreenFacade](curvipy._screen.ScreenFacade) on the [Documentation](documentation.md) section).

Thanks to this class, the plotter can work with *logical points* (also known as *virtual points*), i.e. the actual mathematical coordinates of points. Evidently, logical points do not represent the real positions where the points will be drawn on screen, the *real points*. Real points depend on the screen size and the scale of the axes. The [ScreenFacade.get_real_point()](curvipy._screen.ScreenFacade) method translates a logical point to a real point. In other words, it returns the window position on which the logical point sits:

Given a virtual point {math}`P_{v} = (x_{v}, y_{v})`, a real point {math}`P_{r} = (x_{r}, y_{r})`, and the screen real width {math}`w_{r}`, real height {math}`h_{r}`, virtual width {math}`w_{v}` and virtual height {math}`h_{v}`, the function {math}`f: \mathbb{R}^2  \rightarrow \mathbb{R}^2` that maps a virtual point to its respective real point is defined as:

```{math}
f(P_{v}) = (x_{v} \cdot \frac{w_{r}}{w_{v}}, y_{v} \cdot \frac{h_{r}}{h_{v}}) = P_{r}
```