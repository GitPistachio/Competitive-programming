# Project name : SPOJ: RANDMOD - Random modulo n
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  : You derivate formula from nE(n) = (n - 1)E(n - 1) + 1 + H(n - 1) => E(n) = H(n)
# Status       : Accepted (23883992)
# Tags         : python, harmonic series, Euler-Mascheroni constant, Bernoulli number
# Comment      :

from sys import stdin, stdout
from math import log

T = int(stdin.readline())

def h(n):
    val = 0
    if n < 10:
        for i in range(1, n + 1):
            val += 1.0/i
    else:
        gamma = 0.577215664901532860606512090082
        n2 = n*n
        n4 = n2*n2
        val = log(n) + gamma + 0.5/n - 1.0/(12*n2) + 1.0/(120*n4) - 1.0/(252*n4*n2) + 1.0/(240*n4*n4)

    return val


for i in range(T):
    n = int(stdin.readline())
    stdout.write("%.10f\n" % h(n))
