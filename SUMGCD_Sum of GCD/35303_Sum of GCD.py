#Time limit fail

from itertools import combinations
from fractions import gcd

T = int(input())

t = time.time()
for i in range(T):
    n = map(int, input().split(' ')[1:])
    print(sum([gcd(a, b) for a, b in combinations(n, 2)]))
