# Project name : SPOJ: MOZSAS - Shahadat and Sequence
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-16
# Description  :
# Status       : Accepted (23639507)
# Tags         : python
# Comment      :

import sys

def isOddOrEven(tokens):
    l, r = map(int, tokens.split())
    if l & 1 == 0:
        d = (r - l)//2
        if d & 1 == 0:
            return "Odd\n"
        else:
            return "Even\n"
    else:
        d = (r - l + 1)//2
        if d & 1 == 0:
            return "Even\n"
        else:
            return "Odd\n"

n = int(input())
input()
T = int(input())

sys.stdout.write(''.join(map(isOddOrEven, sys.stdin)))
