# Project name : SPOJ: PIVAL - Digits of Pi
# Author       : Wojciech Raszka
# Date created : 2020-04-06
# Description  :
# Status       : Accepted (27662459)
# Tags         : python, pi, streaming algorithm, spigot algorithm, unbounded spigot algorithm for the digits of pi
# Comment      : 9002

from sys import stdin, stdout

def getPiDigits():
    '''Unbounded spigot algorithm for the digits of pi by Jeremy Gibbons.'''
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (10*q, 10*(r - n*t), t, k, (10*(3*q + r))//t - 10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q + r)*l, t*l, k + 1, (q*(7*k + 2) + r*l)//(t*l), l + 2)

NDIGITS = 2000
pi_digits = getPiDigits()

stdout.write('{}.'.format(next(pi_digits)))
for _ in range(NDIGITS):
    stdout.write('{}'.format(next(pi_digits)))
    
stdout.write('\n')