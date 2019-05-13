# Project name : SPOJ: JADDOU3 - Jaddouic Sequence
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-05-12
# Description  :
# Status       : Accepted (23754408)
# Tags         : python, modulo power, integer sequence A007582 (OEIS)
# Comment      :

import sys


def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            result = (result * x) % p

        y = y >> 1
        x = (x * x) % p

    return result

n = int(sys.stdin.readline())

p = 123456789
a_n = power(2, n - 1, p)
b_n = (2*a_n*a_n + a_n) % p

sys.stdout.write(str(b_n))
