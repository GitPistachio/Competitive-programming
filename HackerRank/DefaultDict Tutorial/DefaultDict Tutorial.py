# Project name : HackerRank: DefaultDict Tutorial
# Link         : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-17
# Description  :
# Status       : Accepted (209190401)
# Tags         : python
# Comment      : 

from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)
for i in range(n):
    A[input()].append(str(i + 1))

for _ in range(m):
    b = input()
    if b in A:
        print(' '.join(A[b]))
    else:
        print('-1')
