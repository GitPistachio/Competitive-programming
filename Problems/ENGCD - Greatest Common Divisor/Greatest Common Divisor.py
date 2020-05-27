# Project name : SPOJ: ENGCD - Greatest Common Divisor
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483764)
# Tags         : python, GCD, greatest common divisor
# Comment      :

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

print(gcd(int(input()), int(input())))
