# Project name : SPOJ: CPTTRN2 - Character Patterns (Act 2)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted(23283688)
# Comment      :

def drawPattern(n, m):
    if n > 0:
        print("*"*m)
    if n > 1:
        if m <= 2:
            inner_row = "*"*m
        else:
            inner_row = "*" + "."*(m-2) + "*"

        for i in range(n - 2):
            print(inner_row)

        print("*"*m)

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    drawPattern(n, m)

    if t + 1 < T:
        print()
