# Project name : SPOJ: CPTTRN1 - Character Patterns (Act 1)
# Author       : Wojciech Raszka
# Date created : 2019-02-23
# Description  :
# Status       : Accepted (23283637)
# Comment      :

def drawPattern(n, m):
    odd = "*."*(m//2) + ("*" if m % 2 == 1 else "")
    even = ".*"*(m//2) + ("." if m % 2 == 1 else "")
    for is_odd in [True, False]*(n//2):
        if is_odd:
            print(odd)
        else:
            print(even)

    if n % 2 == 1:
        print(odd)

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    drawPattern(n, m)

    if t + 1 < T:
        print()
