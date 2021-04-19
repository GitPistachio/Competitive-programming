# Project name : HackerRank: Gemstones
# Link         : https://www.hackerrank.com/challenges/gem-stones/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-19
# Description  :
# Status       : Accepted (209531287)
# Tags         : python
# Comment      : 

from string import ascii_lowercase

n = int(input())

gemstones = set(ascii_lowercase)
for _ in range(n):
    s = input().rstrip()
    for gemstone in gemstones.copy():
        if gemstone not in s:
            gemstones.remove(gemstone)
    
print(len(gemstones))
