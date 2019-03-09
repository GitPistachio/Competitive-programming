# Project name : SPOJ: MADODDSUM - Easy Odd Sum
# Author       : Wojciech Raszka
# Date created : 2019-03-08
# Description  :
# Status       : Accepted (23367652)
# Comment      :

a, b = map(int, input().split())

a += (a + 1) % 2
b -= (b + 1) % 2

if b >= a:
    n = (b - a)//2 + 1
    print((a + b)//2*n)
else:
    print(0)
