# Project name : SPOJ: CODEM1 - Problem1
# Author       : Wojciech Raszka
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23370155)
# Comment      : The question should be: Is it possible to determine if sum of given three numbers is positive, negative or 0

T = int(input())

def NVL(a, b, c):
    if a == '$' and b == '$':
        return c
    elif a == '$':
        return b
    else:
        return a

for t in range(T):
    a,b,c = list(input())
    if NVL(a, b, c) == NVL(b, c, a) == NVL(c, a, b):
        print('possible')
    else:
        print('trivial')
