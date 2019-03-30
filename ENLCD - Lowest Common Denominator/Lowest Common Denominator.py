# Project name : SPOJ: ENLCD - Lowest Common Denominator
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483754)
# Tags         : python, LCM, lowest common denominator, GCD, greatest common divisor
# Comment      :

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a*b//gcd(a, b)

print(lcm(int(input()), int(input())))
