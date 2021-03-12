# Project name : SPOJ: SOD - Sum of Divisors
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-12
# Description  :
# Status       : Accepted (27545878)
# Tags         : python, math, sum of divisors, prime factoriztion, prime numbers, geometric series
# Comment      : Sum of divisors sigma(n) = simga(p_1^k_1*p_2^k_2...p_i^k_i) = sigma(p_1^k_1)*sigma(p_2^k_2)*...*simga(p_i^k_i). Also sigma(p^k) = (p^(k - 1) - 1)/(p - 1)

from sys import stdin, stdout
 
no_of_prime_factors = int(stdin.readline())
 
sod = 1
for _ in range(no_of_prime_factors):
    p, k = map(int, stdin.readline().split())
    sod *= (p**(k + 1) - 1)//(p - 1)
 
stdout.write('{}\n'.format(sod))