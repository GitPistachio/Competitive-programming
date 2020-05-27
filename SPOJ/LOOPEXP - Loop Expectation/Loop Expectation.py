# Project name : SPOJ: LOOPEXP - Loop Expectation
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-28
# Description  :
# Status       : Accepted (23694557)
# Tags         : python, combinatorics, math, integer sequence A000254 (OEIS), unsigned Stirling numbers of first kind, harmonic series, prefix sum
# Comment      : c(n) = sum of fisrt n terms of harmonic series. To derivate this have to obsere than c(n) = a(n)/b(n) where
# Comment      : a(n) is the sum of the if block execution for all permutation of [1,2,...,n] and b(n) is the number of this permutations.
# Comment      : The number of permutation of [1,2,...,n] is equal to n!, thus b(n) = n!. A(n) is more complex, if we observe the pattern a(n) is eqaul to
# Comment      : number of permutation of [1,2,...,n,n+1], where if block for these permutations is executed exacly 2 times. These permutations are nothing but
# Comment      : a number of permutations with two cycles and this is the unsigned Stirling number of first kind for two cycles, thus a(n) = n*a(n - 1) + (n - 1)!
# Comment      : c(n) = a(n)/b(n) = (n*a(n - 1) * (n - 1)!)/n! = a(n - 1)/(n-1)! + 1/n = sum of first n term of harmonic series

import sys

MAX_N = 100000

H = [0.]*(MAX_N + 1)

for n in range(1, MAX_N + 1):
    H[n] = H[n - 1] + 1.0/n


T = int(sys.stdin.readline())

while T > 0:
    n = int(sys.stdin.readline())

    sys.stdout.write("%.6f\n" % H[n])
    T -= 1
