import numpy as np

from intervals import Interval

class Gauge:

    def __init__(self, func, interval):
        self.delta = func
        self.interval = interval
        self.__validate__()

    def __validate__(self):
        for x in self.interval.discretize():
            assert self.delta(x) > 0

    def __call__(self, x):
        assert self.interval.contains(x)
        return self.delta(x)

    @staticmethod
    def constant(delta):
        assert delta > 0
        return Gauge(lambda:delta, Interval(-np.inf, np.inf, closed=False, iters=1))