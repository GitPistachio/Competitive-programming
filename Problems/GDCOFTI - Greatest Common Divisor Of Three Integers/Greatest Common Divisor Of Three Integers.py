# Project name : SPOJ: GDCOFTI - Greatest Common Divisor Of Three Integers
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-12
# Description  :
# Status       : Accepted (23634304)
# Tags         : python, GCD, greatest common divisor
# Comment      :

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

a = int(input())
b = int(input())
c = int(input())

print(gcd(gcd(a, b), c))
