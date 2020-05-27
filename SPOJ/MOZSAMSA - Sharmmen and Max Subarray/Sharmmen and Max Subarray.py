# Project name : SPOJ: MOZSAMSA - Sharmmen and Max Subarray
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-22
# Description  :
# Status       : Accepted (23669830)
# Tags         : python
# Comment      :

from functools import reduce

def maxSubarrayLength(x, y):
    global m
    global t

    if x != y:
        t = 1
    else:
        t += 1
        if t > m:
            m = t

    return y

T = int(input())

while T > 0:
    n = int(input())
    if n == 1:
        input()
        print(1)
    else:
        m, t = 1, 1
        reduce(maxSubarrayLength, input().split())

        print(m)
    T -= 1
