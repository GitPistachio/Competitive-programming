# Project name : SPOJ: Game store
# Author       : Wojciech Raszka
# Date created : 2019-02-10
# Description  :
# Status       : Accepted (23207470)
# Comment      :


from math import ceil
from fractions import gcd

N, K = input().split()
N, K = int(N), int(K)

while K != -1 and N != -1:
    #p = N*(N - 1) - (N - 1)*(N - K) - (2*N - K + 1)*K//2 + ceil(K/2)
    p = (K*(K - 1)//2 - K//2)//2
    #q = N*(N - 1)
    q = N*(N - 1)//2

    if p == 0:
        print(0)
    else:
        nwd = gcd(p, q)
        print(p//nwd, "/", q//nwd, sep="")

    N, K = input().split()
    N, K = int(N), int(K)
