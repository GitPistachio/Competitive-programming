# Project name : HackerRank: itertools.combinations_with_replacement()
# Link         : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-10-03
# Description  :
# Status       : Accepted (182391730)
# Tags         : python
# Comment      : 

from itertools import combinations_with_replacement

text, k = input().split()

cmbs = combinations_with_replacement(sorted(text), r=int(k))

print(*list(map(lambda x: ''.join(x), cmbs)), sep="\n")
