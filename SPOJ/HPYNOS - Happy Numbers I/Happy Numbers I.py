# Project name : SPOJ: HPYNOS - Happy Numbers I
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-16
# Description  :
# Status       : Accepted (23927784)
# Tags         : python
# Comment      :

from sys import stdin, stdout

def sumOfDigitSquares(n):
    result = 0;

    while n > 0:
        r = n % 10
        result += r*r
        n //= 10;

    return result

def checkIfHappy(n):
    not_happy_at_all = {4, 16, 20, 37, 42, 58, 89, 145}

    while True:
        if n in not_happy_at_all:
            return -1
            break
        elif n != 1:
            cnt = checkIfHappy(sumOfDigitSquares(n))
            if checkIfHappy(sumOfDigitSquares(n)) != -1:
                return cnt + 1
            else:
                return -1
        else:
            return 0

n = int(stdin.readline())

stdout.write('%d\n' % checkIfHappy(n))
