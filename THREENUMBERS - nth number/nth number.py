# Project name : SPOJ: BOKAM143SOU - Checking cubes.
# Author       : Wojciech Raszka
# Date created : 2019-03-22
# Description  :
# Status       : Accepted (23476698)
# Tags         : python, binary search, gcd, greatest common divisor
# Comment      : Problem setter gave incorrect input. There is less test than T.

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def findNthNumber(a, b, d, n, l, r):
    m = l + (r - l + 1)//2

    t = m//a + m//b - m//(a*b//d)
    if t == n:
        return m - min(m % a, m %  b, m % (a*b//d))
    elif t > n:
        return findNthNumber(a, b, d, n, l, m)
    else:
        return findNthNumber(a, b, d, n, m, r)


T = int(input())

for t in range(T):
    try:
        a, b, n = map(int, input().split())
        d = gcd(a, b)
        if a % b == 0:
            result = b*n
        elif b % a == 0:
            result = a*n
        else:
            result = findNthNumber(a, b, d, n, max(min(a, b), n), min(a, b)*n)
        print(result)
    except:
        print(result)
