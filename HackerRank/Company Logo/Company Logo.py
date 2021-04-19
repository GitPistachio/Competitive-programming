# Project name : HackerRank: Company Logo
# Link         : https://www.hackerrank.com/challenges/most-commons/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-18
# Description  :
# Status       : Accepted (209380806)
# Tags         : python
# Comment      : 

from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(s)
    for letter, count in sorted(c.items(), key=lambda pair: (-pair[1], pair[0]))[:3]:
        print(letter, count)
