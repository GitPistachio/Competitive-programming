# Project name : HackerRank: Day 25: Running Time and Complexity
# Link         : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-13
# Description  :
# Status       : Accepted (168695895)
# Tags         : python, prime numbers, number theory
# Comment      : 

from sys import stdin, stdout

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
            
        i += 2
    
    return True

no_of_tests = int(stdin.readline())

for _ in range(no_of_tests):
    n = int(stdin.readline())
    if isPrime(n):
        stdout.write('Prime\n')
    else:
        stdout.write('Not prime\n')
