# Project name : HackerRank: itertools.permutations()
# Link         : https://www.hackerrank.com/challenges/itertools-permutations/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-10-02
# Description  :
# Status       : Accepted (182319358)
# Tags         : python
# Comment      : 

from itertools import permutations

text, k = input().split()

pmt = list(permutations(sorted(text), r=int(k)))


print('\n'.join(map(lambda x: ''.join(x), pmt)))
