# Project name : HackerRank: itertools.combinations()
# Link         : https://www.hackerrank.com/challenges/itertools-combinations/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-10-02
# Description  :
# Status       : Accepted (182321738)
# Tags         : python
# Comment      : 

from itertools import combinations

text, k = input().split()


for r in range(1, int(k) + 1):
    cmbs = combinations(sorted(text), r=r)

    print(*list(map(lambda x: ''.join(x), cmbs)), sep="\n")
