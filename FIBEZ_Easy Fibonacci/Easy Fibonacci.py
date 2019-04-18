# Project name : SPOJ: FIBEZ - Easy Fibonacci
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-07
# Description  :
# Status       : Accepted (23369217)
# Tags         : python, fibonacci sequence
# Comment      : PYPY 2.7

from sys import stdin, stdout
from math import log

def fibonacci(n, p):
    if n:
        a, b = fibonacci(n/2, p)
        c = (a * (b * 2 - a)) % p
        d = (a * a + b * b) % p
        if n % 2 == 0:
        	return (c, d)
        else:
        	return (d, c + d)
    else:
        return (0, 1)

p = 100000007
max_n = 500000
T = int(raw_input())

F = [0]*(max_n + 1)
F[1] = 1

for i in xrange(2, max_n + 1):
    F[i] = (F[i - 1] + F[i - 2]) % p

if T > max_n/log(max_n, 2):
    F = [0]*(max_n + 1)
    F[1] = 1

    for i in xrange(2, max_n + 1):
        F[i] = (F[i - 1] + F[i - 2]) % p

    for n in stdin.readlines():
        stdout.write(str(F[int(n)]))
        stdout.write('\n')
else:
    for n in stdin.readlines():
        stdout.write(str(fibonacci(int(n), p)[0]))
        stdout.write('\n')
