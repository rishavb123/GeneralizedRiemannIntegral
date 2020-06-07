from sys import argv

from intervals import *
from partitions import *
from gauge import Gauge

class Test:

    @staticmethod
    def intervals():
        A = Interval(0, 5)
        B = Interval(4, 10, closed=False)
        C = Interval.intersection(A, B)
        D = Interval.union(A, B)

        print(A, B, len(A), B.size())
        print(C, D)
        print(Union((C, D)))
        print()

        def test(I):
            print(I)
            print("Contains 4:", I.contains(4))
            print("Contains 5:", 5 in I)
            print()

        test(A)
        test(B)
        test(C)
        test(D)
    
    @staticmethod
    def partitions():
        end = 10
        I = Interval(0, end)
        P = Partition([i for i in range(end + 1)], I)
        T = P.tag([i + 0.5 for i in range(end)])

        print("Interval:", I)
        print("Partition:", P)
        print("Tagged Partition:", T)

    @staticmethod
    def gauges():
        end = 10
        I = Interval(0, end, closed=False)
        G = Gauge(lambda x: 2 * x, I)
        print(G(2))
        C = Gauge.constant(2)
        print(C(10000))

    @staticmethod
    def delta_fine():
        end = 10
        I = Interval(1, end)
        G = Gauge(lambda x: x ** 2 / 120, I)
        T = TaggedPartition.generate_delta_fine(I, G)
        print(T, T.is_delta_fine(G))
        last_c = -1
        for c in np.arange(10, 0, -0.001):
            if not T.is_delta_fine(Gauge.constant(c)):
                print(last_c)
                return
            last_c = c


for arg in argv[1:]:
    print('\n---------------------------' + arg.upper() + ' TEST---------------------------')
    getattr(Test, arg)()

