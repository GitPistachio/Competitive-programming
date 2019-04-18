# Project name : SPOJ: M3TILE - LATGACH3
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-14
# Description  :
# Status       : Accepted (23634235)
# Tags         : python, integer sequence A001835 (OEIS)
# Comment      : 

def a(n):
    if n == 0 or n == 1:
        return 1

    return 4*a(n - 1) - a(n - 2)


while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(1)
    elif n & 1:
        print(0)
    else:
        print(a(n//2 + 1))
