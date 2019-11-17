# Project name : SPOJ: MAGGNUM - Trova il numero maggiore
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-27
# Description  :
# Status       : Accepted (23506348)
# Tags         : python, gcd, greatest common divisor
# Comment      :

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

A = eval(input())

print(gcd(A[0], A[1]))
