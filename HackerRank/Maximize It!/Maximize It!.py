# Project name : HackerRank: Maximize It!
# Link         : https://www.hackerrank.com/challenges/maximize-it/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-18
# Description  :
# Status       : Accepted (209376068)
# Tags         : python
# Comment      : 

from itertools import product

K, M = map(int, input().split())

A = []
for _ in range(K):
    A.append(map(int, input().split()[1:]))

max_s = 0
for p in product(*A):
    s = sum(map(lambda x: x*x, p)) % M
    if s > max_s:
        max_s = s

print(max_s)
