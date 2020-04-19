class CustomInterval:
    def contains(self, x):
        print("Using default contains method, please override this")
        return False

    @staticmethod
    def union(i1, i2):
        return Union((i1, i2))

    @staticmethod
    def intersection(i1, i2):
        return Intersection((i1, i2))


class Interval(CustomInterval):

    EMPTY = Interval(0, 0, closed=False)

    def __init__(self, a, b, closed=True):
        self.__a = a
        self.__b = b
        self.__closed = closed
        self.size = b - a
        self.C = Union((Interval(float("-inf"), a, closed=not closed), Interval(b, float("inf"), closed=not closed)))

    def contains(self, x):
        return self.__a <= x <= self.__b if self.__closed else self.__a < x < self.__b

    def __str__(self):
        return ('[' if self.__closed else '(') + str(self.__a) + ", " + str(self.__b) + (']' if self.__closed else ')')

    @staticmethod
    def single_value(x):
        return Interval(x, x)

class Union(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        for i in intervals:
            if i.contains(x): return True
        return False

    def __str__(self):
        return ' U '.join([str(i) for i in intervals])

class Intersection(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        for i in intervals:
            if not i.contains(x): return False
        return True

    def __str__(self):
        return ' ⋂ '.join([str(i) for i in intervals])