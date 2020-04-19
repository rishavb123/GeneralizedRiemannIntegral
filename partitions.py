from intervals import Interval

class Partition:

    def __init__(self, nums, interval):
        self.nums = nums
        self.nums.sort()
        self.n = len(nums) - 1
        self.interval = interval
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

class TaggedPartition(Partition):

    def __init__(self, nums, interval, c):
        super().__init__(nums, interval)
        self.__c = c
        self.__c.sort()
        self.__validate__()

    def __validate__(self):
        super().__validate__()
        assert self.partition.n == len(self.c)
        for k in range(1, self.partition.n + 1):
            assert self.partition.get_subinterval(k).contains(self.c(k))

    def c(self, k):
        return c[k - 1]