# Project name : SPOJ: ONEZERO - Ones and zeros
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-26
# Description  :
# Status       : Accepted (23689815, 23689829)
# Tags         : python, BFS, breadth first search, iteger sequence A004290 (OEIS)
# Comment      : 0.24s in PYPY

import sys

def getMinimumMultipleOfBinaryDigit(n):
    global A

    f2 = 0
    while n & 1 == 0:
        n = n >> 1
        f2 += 1

    f5 = 0
    while n % 5 == 0:
        n = n//5
        f5 += 1

    if n in A:
        return A[n] + '0'*max(f2, f5)

    visited = set()

    q = [1]
    i = 0
    while True:
        binary_number  = q[i]
        i += 1

        r = binary_number % n

        if r == 0:
            A[n] = str(binary_number)
            return A[n] + '0'*max(f2, f5)
        elif r not in visited:
            visited.add(r)
            q.append(binary_number*10)
            q.append(binary_number*10 + 1)

A = {}
T = int(sys.stdin.readline())
sys.stdout.write('\n'.join(map(lambda n: getMinimumMultipleOfBinaryDigit(int(n)), sys.stdin)) + '\n')
