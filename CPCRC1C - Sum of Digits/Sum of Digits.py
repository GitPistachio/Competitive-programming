# Project name : SPOJ: CPCRC1C - Sum of Digits
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-16
# Description  :
# Status       : Accepted (23925503)
# Tags         : python, sum of digits from 1 to n, integer sequence A037123 (OEIS)
# Comment      :

from sys import stdin, stdout
import math

MAX_NO_OF_DIGITS = 15
A = [0]*(MAX_NO_OF_DIGITS + 1)
A[1] = 45
B = [0]*(MAX_NO_OF_DIGITS + 1)
B[0] = 1
B[1] = 10
for i in range(2, MAX_NO_OF_DIGITS + 1):
    A[i] = A[i - 1]*10 + 45*B[i - 1]
    B[i] = B[i - 1]*10

def sumOfDigitsFrom1ToN(n):
    global A
    global B

    if n < 10:
        return n*(n + 1) >> 1

    no_of_digits = int(math.log10(n))
    msd = n //B[no_of_digits]

    return msd*A[no_of_digits] + (msd*(msd - 1) >> 1)*B[no_of_digits] + msd*(1 + n % B[no_of_digits]) + sumOfDigitsFrom1ToN(n % B[no_of_digits])

for tokens in stdin:
    a, b  = tokens.split()
    a, b = int(a), int(b)

    if a == -1 and b == -1:
        break

    x = sumOfDigitsFrom1ToN(b) - sumOfDigitsFrom1ToN(a - 1)

    stdout.write('%d\n' % x)
