# Project name : CodeChef: FCTRL - Factorial
# Link         : https://www.codechef.com/LRNDSA01/problems/FCTRL
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-05-31
# Description  :
# Status       : Accepted (33527157)
# Tags         : python, number of trailing zeros in n!,  integer sequence A027868 (OEIS), factorial
# Comment      :

def Z(n):
    d = 5
    no_of_zeros = 0
    while d <= n:
        no_of_zeros += n//d
        d *= 5

    return no_of_zeros

T = int(input())
N = [int(input()) for i in range(T)]

for n in N:
    print(Z(n))
