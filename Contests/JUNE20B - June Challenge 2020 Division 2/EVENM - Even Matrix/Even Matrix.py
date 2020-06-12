# Project name : CodeChef: EVENM - Even Matrix
# Link         : https://www.codechef.com/JUNE20B/problems/EVENM
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-05
# Description  :
# Status       : Accepted (33732001)
# Tags         : python, matrix
# Comment      : 100

from sys import stdin, stdout


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n = int(stdin.readline())

    a = 1
    if n & 1 == 0:
        for i in range(1, n + 1):
            if i & 1 == 0:
                row = range(a + n - 1, a - 1, -1)
            else:
                row = range(a, a + n)
            stdout.write(' '.join(map(str, row)) + "\n")
            a += n
    else:
        for i in range(1, n + 1):
            row = range(a, a + n)
            stdout.write(' '.join(map(str, row)) + "\n")
            a += n
