# Project name : SPOJ: CPTTRN6 - Character Patterns (Act 6)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23284441)
# Comment      :

def drawPattern(n, m, h, w):
    for i in range(n):
        for j in range(h):
            print('|'.join(['.'*w]*(m + 1)))
        if i + 1 < n:
            print('+'.join(['-'*w]*(m + 1)))


T = int(input())

for t in range(T):
    n, m, h, w = map(int, input().split())
    drawPattern(n + 1, m, h, w)

    if t + 1 < T:
        print()
