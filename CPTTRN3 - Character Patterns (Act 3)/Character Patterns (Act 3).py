# Project name : SPOJ: CPTTRN3 - Character Patterns (Act 3)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23283814)
# Comment      :

def drawPattern(n, m):
    print("*"*(3*m + 1))
    inner_row = "*.."*m + "*"
    for i in range(n):
        print(inner_row)
        print(inner_row)
        print("*"*(3*m + 1))

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    drawPattern(n, m)

    if t + 1 < T:
        print()
