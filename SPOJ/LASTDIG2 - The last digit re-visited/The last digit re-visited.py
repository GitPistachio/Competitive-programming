# Project name : SPOJ: LASTDIG2 - The last digit re-visited
# Author       : Wojciech Raszka
# Date created : 2019-04-01
# Description  :
# Status       : Accepted (23545539)
# Tags         : python, number theory, last digit, big numbers
# Comment      : pypy

C=(0,0,0,0,1,1,1,1,2,4,8,6,3,9,7,1,4,6,4,6,5,5,5,5,6,6,6,6,7,9,3,1,8,4,2,6,9,1,9,1)
T = int(raw_input())

for t in range(T):
    a, b = raw_input().split()
    a = int(a[-1])
    b = int(b)

    if a == b:
        print 0
    elif b == 0:
        print 1
    else:
        b = (b - 1)% 4
        print C[4*a + b]
