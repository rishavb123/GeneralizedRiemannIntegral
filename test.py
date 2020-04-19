from intervals import *

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