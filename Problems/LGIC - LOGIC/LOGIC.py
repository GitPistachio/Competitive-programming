# Project name : SPOJ: LGIC - LOGIC
# Author       : Wojciech Raszka
# Date created : 2019-03-30
# Description  :
# Status       : Accepted (23526325)
# Tags         : python, factorial
# Comment      :

def getNthTerm(n):
    a = 1
    b = 1
    for i in range(2, n + 1):
        a *= i
        b = 2*b + i - 2

    return a + b


n = int(input())

print(getNthTerm(n))
