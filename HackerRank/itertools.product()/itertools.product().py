# Project name : HackerRank: itertools.product()
# Link         : https://www.hackerrank.com/challenges/itertools-product/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-10-01
# Description  :
# Status       : Accepted (182148105)
# Tags         : python
# Comment      : 

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

AxB = list(product(A, B))

print(*AxB, sep=" ")
