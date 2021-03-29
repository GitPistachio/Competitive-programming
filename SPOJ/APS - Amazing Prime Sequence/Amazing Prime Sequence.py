# Project name : SPOJ: APS - Amazing Prime Sequence
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-04-28
# Description  :
# Status       : Accepted (23694169)
# Tags         : python, math, number theory, 2-3-5 wheel factorization, sieve of eratosthenes, prefix sum, integer sequence A020639 (OEIS), least prime dividing n, integer sequence A088821 (OEIS), dynamic programming
# Comment      : For calculation of f(n) it was used modified modified sieve of eratosthenes with 2-3-5 wheel factorization where nth term if is 0 mean than n is prime otherwise nth therm is the least prime dividing n

import sys

MAX_N = 10000000
least_prime_divisor = [0]*(MAX_N + 1)
wheel = [6,4,2,4,2,4,6,2]
primes = [2,3,5,7,11,13,17,19,23,29,31]

for k in primes:
    for i in range(k*k, MAX_N + 1, k):
        if least_prime_divisor[i] == 0: #to forbid overwriting the least prime factor
            least_prime_divisor[i] = k

run = True
p = 31
while run:
    for w in wheel:
        p += w
        if p*p > MAX_N:
            run = False
            break
        if least_prime_divisor[p] == 0:
            for i in range(p*p, MAX_N + 1, p):
                if least_prime_divisor[i] == 0: #to forbid overwriting the least prime factor
                    least_prime_divisor[i] = p
moving_sum = 0
def a(n):
    global moving_sum
    global least_prime_divisor

    moving_sum += least_prime_divisor[n] if least_prime_divisor[n] > 0 else n

    return moving_sum

A = [a(n) for n in range(2, MAX_N + 1)]

T = int(sys.stdin.readline())

while T > 0:
    n = int(sys.stdin.readline())

    if n < 2:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("%d\n" % A[n - 2])

    T -= 1
