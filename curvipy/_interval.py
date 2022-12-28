from typing import Union as _Union

_TNumber = _Union[int, float]


class Interval:
    """Interval in which a curve will be plotted.

    The interval is splitted into a list of values in which the curve will be evaluated. \
    These values are defined by the number of `samples` specified. The more samples, the \
    more precise the curve plot is.
    
    Parameters
    ----------
    start : int or float
        Real number in which the interval starts.
    end : int or float
        Real number in which the interval ends.
    samples: int
        Number of values within the interval. The more samples, the more precise the \
        curve plot is.
    """

    def __init__(self, start: _TNumber, end: _TNumber, samples: int):
        dx = (end - start) / samples
        self.__interval = [start + dx * i for i in range(samples)]

    def __iter__(self):
        return iter(self.__interval)
