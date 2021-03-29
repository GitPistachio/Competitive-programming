# Project name : SPOJ: FCTRL2 - Small factorials
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 
# Description  :
# Status       : 
# Tags         : python
# Comment      :

def factorial(n):
    if n > 1:
        return n*factorial(n - 1)

    return 1

test_cases = int(input())
numbers = [int(input()) for tc in range(test_cases)]

for n in numbers:
    print(factorial(n))
