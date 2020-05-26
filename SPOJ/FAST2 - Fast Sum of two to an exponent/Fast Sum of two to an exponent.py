# Project name : SPOJ: FAST2 - Fast Sum of two to an exponent
# Author       : Wojciech Raszka
# Date created : 2019-03-18
# Description  :
# Status       : Accepted (23441642)
# Comment      : Precomputed prefix sum

from sys import stdin, stdout

mod = 1298074214633706835075030044377087

T = int(stdin.readline())

X = [1]
Y = [1]
for i in range(500):
    X.append((2*X[i]) % mod)
    Y.append((Y[i] + X[i + 1]) % mod)

stdout.write('\n'.join(map(lambda n: str(Y[int(n)]), stdin)))
