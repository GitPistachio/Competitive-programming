# Project name : SPOJ: PLAYGAME - PLAYGAME
# Author       : Wojciech Raszka
# Date created : 2019-02-17
# Description  :
# Status       : Accepted (23250688)
# Tags         : python
# Comment      : f <=> g

T = int(input())

def g(n):
    if n > 5:
        return not max(g(n - 1), g(n - 2), g(n - 5))
    elif n == 1 or n == 2 or n == 4 or n == 5:
        return True
    else:
        return False

def f(n):
    if n % 3 == 0:
        return False
    else:
        return True

for t in range(T):
    if f(int(input())):
        print("Hemlata")
    else:
        print("Ragini")
