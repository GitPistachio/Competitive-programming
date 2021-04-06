# Project name : SPOJ: PIVAL - Digits of Pi
# Author       : Wojciech Raszka
# Date created : 2020-04-06
# Description  :
# Status       : Accepted (27662515)
# Tags         : python, pi, streaming algorithm, spigot algorithm, bounded spigot algorithm for the digits of pi
# Comment      : 6001

from sys import stdin, stdout

def getPiDigits(no_of_digits):
    '''Bounded spigot algorithm for the digits of pi by Rabinowitz and Wagon. Max no of digits is 15536'''
    LEN = (no_of_digits//4 + 1)*14

    a = [0 for _ in range(LEN)]
    d, e, f, h = 0, 0, 10000, 0
    for c in range(LEN - 14, 0, -14):
        for b in range(c - 1, 0, -1):
            d *= b
            if h == 0:
                d += 2000*f
            else:
                d += a[b]*f
            
            g = b + b - 1
            a[b] = d % g
            d //= g
        
        h = e + d//f
        yield h
        d = e = d % f

NDIGITS = 2000
pi_digits = getPiDigits(NDIGITS)

stdout.write('3.141')
next(pi_digits)
for digits in pi_digits:
    stdout.write('{:04d}'.format(digits))
    
stdout.write('\n')