# Project name : SPOJ: CPTTRN4 - Character Patterns (Act 4)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23283889)
# Comment      :

def drawPattern(n, m, h, w):
    print("*"*((1 + w)*m + 1))
    inner_row = ("*" + "."*w)*m + "*"
    for i in range(n):
        for j in range(h):
            print(inner_row)
        print("*"*((1 + w)*m + 1))

T = int(input())

for t in range(T):
    n, m, h, w = map(int, input().split())
    drawPattern(n, m, h, w)

    if t + 1 < T:
        print()
