import numpy as np

class CustomInterval:

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.size()

    def __iter__(self):
        return self.discritize().__iter__()

    def discretize(self):
        print("Using default discritize method, please override this")
        return []

    def contains(self, x):
        print("Using default contains method, please override this")
        return False

    def size(self):
        print("Using default size method, please override this")
        return -1

    @staticmethod
    def union(i1, i2):
        return Union((i1, i2))

    @staticmethod
    def intersection(i1, i2):
        return Intersection((i1, i2))


class Interval(CustomInterval):

    def __init__(self, a, b, closed=True, iters=1000):
        self.__a = a
        self.__b = b
        self.__closed = closed
        self.__size = b - a
        self.__iters = iters
        self.__discrete = None

        self.__validate__()

    def __validate__(self):
        assert self.__b >= self.__a

    def contains(self, x):
        return self.__a <= x <= self.__b if self.__closed else self.__a < x < self.__b

    def size(self):
        return self.__size

    def get_bounds(self):
        return self.__a, self.__b

    def discretize(self):
        if self.__discrete is None:
            a = self.__a
            b = self.__b
            if a == b:
                self.__discrete = []
            else:
                if abs(a) == np.inf:
                    a = 9999999 * np.sign(a)
                if abs(b) == np.inf:
                    b = 9999999 * np.sign(b)
                s = (b - a) / self.__iters
                self.__discrete = list(np.arange(a, b + s, s) if self.__closed else np.arange(a + s, b, s))
        return self.__discrete

    def __str__(self):
        return ('[' if self.__closed else '(') + str(self.__a) + ", " + str(self.__b) + (']' if self.__closed else ')')

    @staticmethod
    def single_value(x):
        return Interval(x, x)

class Union(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals
        self.__discrete = None

    def contains(self, x):
        for i in self.intervals:
            if i.contains(x): return True
        return False

    def discretize(self):
        if self.__discrete is None:
            self.__discrete = []
            for interval in self.intervals:
                self.__discrete += interval.discretize()
            self.__discrete = list(set(self.__discrete))
            self.__discrete.sort()
        return self.__discrete

    def __str__(self):
        return '(' + ') U ('.join([str(i) for i in self.intervals]) + ')'

class Intersection(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals
        self.__discrete = None

    def contains(self, x):
        for i in self.intervals:
            if not i.contains(x): return False
        return True

    def discretize(self):
        if self.__discrete is None:
            self.__discrete = []
            for val in Union(self.intervals).discretize():
                if self.contains(val):
                    self.__discrete.append(val)
        return self.__discrete

    def __str__(self):
        return '(' + ') n ('.join([str(i) for i in self.intervals]) + ')'

def C(CustomInterval):

    def __init__(self, interval):
        self.interval = interval

    def contains(self, x):
        return not self.interval.contains(x)

    def __str__(self):
        return '(' + str(self.interval) + ')^C'

EMPTY = Interval(0, 0)
R = Interval(-np.inf, np.inf, closed=False)