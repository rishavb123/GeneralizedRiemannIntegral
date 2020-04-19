class CustomInterval:

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.size()

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

    def __init__(self, a, b, closed=True):
        self.__a = a
        self.__b = b
        self.__closed = closed
        self.__size = b - a

    def contains(self, x):
        return self.__a <= x <= self.__b if self.__closed else self.__a < x < self.__b

    def size(self):
        return self.__size

    def __str__(self):
        return ('[' if self.__closed else '(') + str(self.__a) + ", " + str(self.__b) + (']' if self.__closed else ')')

    @staticmethod
    def single_value(x):
        return Interval(x, x)

    @staticmethod
    def empty():
        return Interval(0, 0)

class Union(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        for i in self.intervals:
            if i.contains(x): return True
        return False

    def __str__(self):
        return '(' + ') U ('.join([str(i) for i in self.intervals]) + ')'

class Intersection(CustomInterval):

    def __init__(self, intervals):
        self.intervals = intervals

    def contains(self, x):
        for i in self.intervals:
            if not i.contains(x): return False
        return True

    def __str__(self):
        return '(' + ') n ('.join([str(i) for i in self.intervals]) + ')'

def C(CustomInterval):

    def __init__(self, interval):
        self.interval = interval

    def contains(self, x):
        return not self.interval.contains(x)

    def __str__(self):
        return '(' + str(self.interval) + ')^C'