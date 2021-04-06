# Project name : SPOJ: PIVAL - Digits of Pi
# Author       : Wojciech Raszka
# Date created : 2020-04-06
# Description  :
# Status       : Accepted (27662515)
# Tags         : python, pi, streaming algorithm, spigot algorithm, bounded spigot algorithm for the digits of pi
# Comment      : 5001

from sys import stdin, stdout

def getPiDigits(no_of_digits):
    '''Bounded spigot algorithm for the digits of pi by Rabinowitz and Wagon. Dik Winter and Achim Flammenkamp. Max no of digits is 32372'''
    LEN = (no_of_digits//4 + 1)*14

    b, d, e, f, g, h, i = 0, 0, 0, 10000, 0, 0, 0
    a = [0 for _ in range(LEN)]
    
    for c in range(LEN - 14, 0, -14):
        b = c - 1
        g = b + b
        while g > 0:
            if h == 0:
                d = i*b + f*f//5
            else:
                d = i*b + f*a[b]
            
            g -= 1
            i, a[b] = divmod(d, g)
            b -= 1
            g = b + b
        
        h = e + d//f
        yield h
        e = d % f

NDIGITS = 2000
pi_digits = getPiDigits(NDIGITS)

stdout.write('3.141')
next(pi_digits)
for digits in pi_digits:
    stdout.write('{:04d}'.format(digits))
    
stdout.write('\n')