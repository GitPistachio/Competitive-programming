# Project name : SPOJ: CODEM3 - Problem3
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-04
# Description  :
# Status       : Accepted (23586479)
# Tags         : python
# Comment      :

from functools import reduce

def solve(x, y):
    global is_zero_appeard

    if not isinstance(x, int):
        if x == '0':
            is_zero_appeard = True

        x = 0

    if is_zero_appeard and y != '0':
        return x + 1
    elif y == '0':
        is_zero_appeard = True
        return x
    else:
        return x


T = int(input())

for t in range(T):
    n = int(input())
    is_zero_appeard = False
    print(reduce(solve, input().split()))
