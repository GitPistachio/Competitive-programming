# Project name : SPOJ: INS17M - Fibonacci and Easy GCD
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-02-26
# Description  :
# Status       : Accepted (23763713)
# Tags         : python, math, GCD, greatest common divisor, fibonacci sequence, pisano period, modulo power, modular arithmetic, fast modular exponentiation
# Comment      : Applying formula GCD(F(a), F(b)) = F(GCD(a, b)) we change problem to calculate n^2 fibonacci numbers. Further it could be reduce to max value of A_i if
# Comment      : we precalculate all possible gcd(A_i, A_j). The maximum no of possible gcd is less than max(A_1, A_2, ..., A_n). The last problem is calculation fibonacci number for
# Comment      : large numbers it could be solve using the fact F(a) mod m = F(r) mod m, where r = a mod pisano period. The pisano period for given modulo is 2000000016

import sys

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

def power(x, k, p):
    res = 1
    x = x % p

    while k:
        if k & 1 == 1:
            res = (res*x) % p

        k = k >> 1
        x = (x*x) % p

    return res

def getPisanoPeriod(m):
    f_0 = 1
    f_1 = 1
    pisano_period = 1
    while f_1 != 1 or f_0 != 0:
        f_0, f_1 = f_1, (f_0 + f_1) % m
        pisano_period += 1

    return pisano_period

def FIBGCD(A, MAX_VALUE, k, m, pisano_period):
    value_no_of_occurences = [0]*(MAX_VALUE + 1)
    for a in A:
        value_no_of_occurences[a] += 1

    divisors_no_of_occurences = [0]*(MAX_VALUE + 1)
    for d in range(1, MAX_VALUE + 1):
        for i in range(d, MAX_VALUE + 1, d):
            divisors_no_of_occurences[d] += value_no_of_occurences[i]

    gcd_no_of_of_occurences = [0]*(MAX_VALUE + 1)
    for d in range(MAX_VALUE, 0, -1):
        if divisors_no_of_occurences[d] != 0:
            gcd_no_of_of_occurences[d] = divisors_no_of_occurences[d]*(divisors_no_of_occurences[d] - 1)//2
            for i in range(d + d, MAX_VALUE + 1, d):
                gcd_no_of_of_occurences[d] -= gcd_no_of_of_occurences[i]


    result = 0
    for d in range(1, MAX_VALUE + 1):
        if gcd_no_of_of_occurences[d] > 0:
            d_k = power(d, k, pisano_period)
            result = (result + gcd_no_of_of_occurences[d] * fibonacci(d_k, m)[0]) % m

    return result


M = 1000000007
PISANO_PERIOD = 2000000016

#sys.stdout.write(str(getPisanoPeriod(M)))

n, k = map(int, sys.stdin.readline().split())

A = [int(x) for x in sys.stdin.readline().split()]
MAX_VALUE = max(A)

sys.stdout.write(str(FIBGCD(A, MAX_VALUE, k, M, PISANO_PERIOD)))
