import numpy as np

from intervals import R

class Gauge:

    def __init__(self, func, interval, validate=True):
        self.delta = func
        self.interval = interval
        if validate:
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
        return Gauge(lambda x:delta, R, validate=False)