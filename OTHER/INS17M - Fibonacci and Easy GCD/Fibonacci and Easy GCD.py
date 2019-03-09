# Project name : SPOJ: INS17M - Fibonacci and Easy GCD
# Author       : Wojciech Raszka
# Date created : 2019-02-26
# Description  :
# Status       :
# Comment      :

def fibonacci(n, p):
    if n:
        a, b = fibonacci(n//2, p)
        c = (a * (b * 2 - a)) % p
        d = (a * a + b * b) % p
        if n % 2 == 0:
        	return (c, d)
        else:
        	return (d, c + d)
    else:
        return (0, 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def power(x, k, p):
    res = 1
    x = x % p

    while k:
        if k & 1 == 1:
            res = (res*x) % p

        k = k >> 1
        x = (x*x) % p

    return res

def S(A, n, k, p):
    res = 0
    for i in xrange(n):
        for j in xrange(i + 1, n):
            x = power(gcd(A[i], A[j]), k, p)
            res += fibonacci(x, p)[0]

    return res % p

p = 1000000007

n, k = map(int, raw_input().split())

A = [int(x) for x in raw_input().split()]

print(S(A, n, k, p))
