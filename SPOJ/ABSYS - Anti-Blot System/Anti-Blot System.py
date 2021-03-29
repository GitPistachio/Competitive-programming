# Project name : SPOJ: ABSYS - Anti-Blot System
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-06-20
# Description  :
# Status       : Accepted (23948176)
# Tags         : python, string manipulation
# Comment      :

from sys import stdin, stdout

def sub(a, b):
    lhs, rhs = a.strip().split('machula')

    return b[len(lhs):len(b) - len(rhs)]


T = int(stdin.readline())

while T > 0:
    stdin.readline()
    formula = stdin.readline();

    rhs, lhs = formula.split('=')

    rhs = rhs.split('+')

    pos = None
    if 'machula' in lhs:
        pos = 3
        val = str(int(rhs[0]) + int(rhs[1]))
        rep = sub(lhs, val)
    elif 'machula' in rhs[0]:
        pos = 1
        val = str(int(lhs) - int(rhs[1]))
        rep = sub(rhs[0], val)
    elif 'machula' in rhs[1]:
        pos = 2
        val = str(int(lhs) - int(rhs[0]))
        rep = sub(rhs[1], val)

    if pos is None:
        stdout.write(formula)
    else:
        stdout.write(formula.replace('machula', rep))

    T -= 1
