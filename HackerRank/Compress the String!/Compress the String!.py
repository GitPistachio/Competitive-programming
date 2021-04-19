# Project name : HackerRank: Compress the String!
# Link         : https://www.hackerrank.com/challenges/compress-the-string/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-16
# Description  :
# Status       : Accepted (209083008)
# Tags         : python
# Comment      : 

from itertools import groupby

S = input()

groups = []
for key, group in groupby(S):
    groups.append('({}, {})'.format(len(list(group)), key))

print(' '.join(groups))
