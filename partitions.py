from intervals import Interval

class Partition:

    def __init__(self, nums, interval, validate=True):
        self.nums = nums
        self.nums.sort()
        self.n = len(nums) - 1
        self.interval = interval
        if validate:
            self.__validate__()
        self.__subintervals = {}

    def __validate__(self):
        for i in range(len(self.nums)):
            assert self.interval.contains(self.nums[i])

    def get_subinterval(self, k):
        assert k > 0
        if k not in self.__subintervals:
            self.__subintervals[k] = Interval(self.nums[k - 1], self.nums[k])
        return self.__subintervals[k]

    def tag(self, c):
        return TaggedPartition(self.nums, self.interval, c)

    def __str__(self):
        return '{' + ' < '.join([str(n) for n in self.nums]) + '}'

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

    def __str__(self):
        return '(' + super().__str__() + ', {' + str(self.__c)[1:-1] + '})'