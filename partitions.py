import numpy as np

from intervals import Interval

class Partition:

    def __init__(self, nums, interval, validate=True):
        self.x = nums
        self.x.sort()
        self.n = len(nums) - 1
        self.interval = interval
        if validate:
            self.__validate__()
        self.__subintervals = {}

    def __validate__(self):
        for i in range(len(self.x)):
            assert self.interval.contains(self.x[i])

    def get_subinterval(self, k):
        assert k > 0 and k <= self.n
        if k not in self.__subintervals:
            self.__subintervals[k] = Interval(self.x[k - 1], self.x[k])
        return self.__subintervals[k]

    def tag(self, c):
        return TaggedPartition(self.x, self.interval, c)

    def __str__(self):
        return '{' + ' < '.join([str(n) for n in self.x]) + '}'

class TaggedPartition(Partition):

    def __init__(self, nums, interval, c):
        super().__init__(nums, interval, validate=False)
        self.__c = c
        self.__c.sort()
        self.__validate__()

    def __validate__(self):
        super().__validate__()
        assert self.n == len(self.__c)
        for k in range(1, self.n + 1):
            assert self.get_subinterval(k).contains(self.c(k))

    def c(self, k):
        return self.__c[k - 1]

    def is_delta_fine(self, delta):
        for k in range(1, self.n + 1):
            if self.x[k] - self.x[k - 1] > delta(self.c(k)):
                return False
        return True

    def __str__(self):
        return '(' + super().__str__() + ', {' + str(self.__c)[1:-1] + '})'

    @staticmethod
    def generate_delta_fine(interval, delta, n=1000):
        assert isinstance(interval, Interval)
        a, b = interval.get_bounds()
        def generate(a, b):
            s = (b - a) / n
            r = np.arange(a, b, s)
            for x in r:
                if b - a < delta(x, validate=False):
                    return [a], [x]
            mid = a + (b - a) / 2
            x1, c1 = generate(a, mid)
            x2, c2 = generate(mid, b)
            return x1 + x2, c1 + c2
        x, c = generate(a, b)
        x.append(b)
        return TaggedPartition(x, interval, c)
