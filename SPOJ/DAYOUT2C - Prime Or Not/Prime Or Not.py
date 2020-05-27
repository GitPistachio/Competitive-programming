# Project name : SPOJ: DAYOUT2C - Prime Or Not
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884322)
# Tags         : python, prime numbers, miller-rabin primality test, modulo power
# Comment      :

from sys import stdin, stdout

def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            result = (result * x) % p

        y = y >> 1
        x = (x * x) % p

    return result


def millerRabinTest(n, d, a):
    x = power(a, d, n)

    if (x == 1 or x == n - 1):
        return True

    while d != n - 1:
        x = (x * x) % n
        d = d << 1

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False

def isPrime(n):
    '''Check n if is a prime for less than 318665857834031151167461'''

    if n == 2 or n == 3:
        return True
    elif n & 1 == 0:
        return False

    d = n - 1
    while  d % 2 == 0:
        d //= 2

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a > n - 2: break

        if millerRabinTest(n, d, a) == False:
            return False

    return True

T = int(stdin.readline())

for t in range(T):
    n = int(stdin.readline())
    if isPrime(n):
        stdout.write("%d is a prime\n" % n)
    else:
        stdout.write("%d is not a prime\n" % n)
