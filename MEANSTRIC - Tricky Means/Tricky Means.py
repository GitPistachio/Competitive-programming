# Project name : SPOJ: MEANSTRIC - Tricky Means
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23289108)
# Comment      :

from math import log, exp
from functools import reduce

def arithmeticMean(An, x, n):
    return (An*n + x)/(n + 1)

def  pythagoreanMeans(Mn, x):
    global n
    n += 1
    x = float(x)
    if isinstance(Mn, str):
        Mn = float(Mn)
        A = arithmeticMean(Mn, x, n)
        lG = arithmeticMean(log(Mn), log(x), n)
        iA = arithmeticMean(1/Mn, 1/x, n)
    else:
        A = arithmeticMean(Mn[0], x, n)
        lG = arithmeticMean(Mn[1], log(x), n)
        iA = arithmeticMean(Mn[2], 1/x, n)

    return (A, lG, iA)


T = int(input())

for t in range(T):
    k = int(input())
    n = 0
    if k > 1:
        X = reduce(pythagoreanMeans, input().split())
        A = round(X[0], 9)
        G = round(exp(X[1]), 9)
        H = round(1/X[2], 9)
    else:
        A = float(input())
        G = A
        H = A
    print('%.9f %.9f %.9f' % (A, G, H))
