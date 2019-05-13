# Project name : SPOJ: VPL0_E - External Sequence
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-05-12
# Description  :
# Status       : Accepted (23754757)
# Tags         : python, number theory, integer sequence A005150 (OEIS), look and say sequence
# Comment      : 329

def b(factor, digit):
    if factor > 0:
        return str(factor) + digit
    else:
        return ''

def a(n):
    if n == 1:
        return '1'

    term = ''
    factor = 0
    last_digit = ''

    for digit in a(n - 1):
        if last_digit == digit:
            factor +=1
        else:
            term += b(factor, last_digit)
            factor = 1

        last_digit = digit

    term += b(factor, digit)

    return term

T = int(input())

for t in range(T):
    n = int(input()) + 1
    print('Scenario #%d: %s' % (t + 1, a(n)))
