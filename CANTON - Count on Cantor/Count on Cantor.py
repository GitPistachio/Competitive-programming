# Project name : SPOJ: CANTON - Count on Cantor
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-24
# Description  :
# Status       : Accepted (23681102)
# Tags         : python, math, Cantor prove of countability of the rational numbers, integer sequence A092542 and A092543 (OEIS)
# Comment      : nth number is A092542(n)/A092543(n)

from math import floor, sqrt

def a(n):
    t = floor((-1 + sqrt(8*n - 7))/2)
    i = n - t*(t + 1)//2
    j = (t*t + 3*t + 4)//2 - n

    if t & 1 == 1:
        return i
    else:
        return j

def b(n):
    t = floor((-1 + sqrt(8*n - 7))/2)
    i = n - t*(t + 1)//2
    j = (t*t + 3*t + 4)//2 - n

    if t & 1 == 1:
        return j
    else:
        return i

T = int(input())

while T > 0:
    n = int(input())

    print("TERM ", n, " IS ", a(n), "/", b(n), sep="")
    T -= 1
