# Project name : SPOJ: TSHOW1 - Amusing numbers
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-18
# Description  :
# Status       : Accepted (23654914)
# Tags         : python, number theory, integer sequence A256291 (OEIS)
# Comment      :

def a(n):
    result = 0
    k = 2
    factor = 1
    while k - 2 <= n:
        if (n + 2) % k < (k >> 1):
            result += 5*factor
        else:
            result += 6*factor

        k = k << 1
        factor *= 10

    return result


T = int(input())

while T > 0:
    n = int(input())
    print(a(n - 1))

    T -= 1
