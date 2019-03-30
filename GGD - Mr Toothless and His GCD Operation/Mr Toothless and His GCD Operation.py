# Project name : SPOJ: GGD - Mr Toothless and His GCD Operation
# Author       : Wojciech Raszka
# Date created : 2019-03-22
# Description  :
# Status       : Accepted (23472800)
# Tags         : python, math, GCD, greatest common divisor
# Comment      : O(1)

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    if n == 2:
        print("Case ", t, ": ", 1, " ", 2, sep='')
    elif n == 3:
        print("Case ", t, ": ", 2, " ", 3, sep='')
    else:
        print("Case ", t, ": ", n//2, " ", n - n % 2, sep='')
