# Project name : SPOJ: CPTTRN5 - Character Patterns (Act 5)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23284194)
# Comment      :

def drawPattern(n, m, s):
    print("*"*((1 + s)*m + 1))
    for i in range(n):
        for j in range(s):
            if i % 2 == 0:
                inner_row = ("*" + "."*j + "\\" + "."*(s - j - 1) + "*" + "."*(s - j - 1) + "/" + "."*j)*(m//2) + "*"
                if m % 2 == 1:
                    inner_row += "."*j + "\\" + "."*(s - j - 1) + "*"
            else:
                inner_row = ("*" + "."*(s - j - 1) + "/" + "."*j + "*" + "."*j + "\\" + "."*(s - j - 1))*(m//2) + "*"
                if m % 2 == 1:
                    inner_row += "."*(s - j - 1) + "/" + "."*j + "*"
            print(inner_row)

        print("*"*((1 + s)*m + 1))

T = int(input())

for t in range(T):
    n, m, s = map(int, input().split())
    drawPattern(n, m, s)

    if t + 1 < T:
        print()
