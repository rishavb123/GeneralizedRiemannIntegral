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
        self.a = a
        self.b = b
        self.closed = closed
        self.size = b - a
        self.C = Union((Interval(float("-inf"), a, closed=not self.closed), Interval(b, float("inf"), closed=not self.closed)))

    def contains(self, x):
        return a <= x <= b if closed else a < x < b

    def __str__(self):
        return ('[' if closed else '(') + str(a) + ", " + str(b) + (']' if closed else ')')

    @staticmethod
    def single_value(x):
        return Interval(x, x)

class Union(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        tag = False
        for i in intervals:
            if i.contains(x): tag = True
        return tag

    def __str__(self):
        return ' U '.join([str(i) for i in intervals])

class Intersection(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        tag = True
        for i in intervals:
            if not i.contains(x): tag = False
        return tag