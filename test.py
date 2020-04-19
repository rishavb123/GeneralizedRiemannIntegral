from intervals import *

A = Interval(0, 5)
B = Interval(4, 10, closed=False)

C = Interval.intersection(A, B)
D = Interval.union(A, B)

print(A, B)
print(C, D)
print(Union((C, D)))
print()

def test(I):
    print(I)
    print("Contains 4:", I.contains(4))
    print("Contains 5:", I.contains(5))
    print()

test(A)
test(B)
test(C)
test(D)