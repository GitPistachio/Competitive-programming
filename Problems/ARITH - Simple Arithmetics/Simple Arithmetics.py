# Project name : SPOJ: ARITH - Simple Arithmetics
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-02
# Description  :
# Status       : Accepted (23865739)
# Tags         : python, pen and paper calculus
# Comment      :

from sys import stdin, stdout

def fFill(expr, clogger, n):
    return clogger*max(0, n - len(expr)) + expr

def penAndPaperCalculation(x, y, opr):
    n = len(x)
    m = len(y)
    nm = max(n, m + 1)
    if opr == '-' or opr == '+':
        if opr == '+':
            z = str(int(x) + int(y))
        else:
            z = str(int(x) - int(y))

        tlen = max(nm, len(z))

        stdout.write(fFill(x, ' ', tlen) + '\n')
        stdout.write(fFill(opr + y, ' ', tlen) + '\n')
        stdout.write(fFill('-'*max(len(z), m + 1), ' ', tlen) + '\n')

        stdout.write(fFill(z, ' ', nm) + '\n')
    else:
        ix = int(x)
        mul = []
        for d in y:
            mul.append(str(int(d)*ix))

        z = str(ix * int(y))
        tlen = max(len(mul) + len(mul[0]) - 1, nm, len(z))

        stdout.write(fFill(x, ' ', tlen) + '\n')
        stdout.write(fFill('*' + y, ' ', tlen) + '\n')

        if len(mul) > 1:
            stdout.write(fFill('-'*max(len(mul[-1]), m + 1), ' ', tlen) + '\n')
            for i in range(len(mul) - 1, -1, -1):
                stdout.write(fFill(mul[i], ' ', tlen - (len(mul) - i - 1)) + '\n')
            stdout.write(fFill('-'*max(len(mul) + len(mul[0]) - 1, len(z)), ' ', tlen) + '\n')
        else:
            stdout.write(fFill('-'*max(nm, len(z)), ' ', tlen) + '\n')
        stdout.write(fFill(z, ' ', tlen) + '\n')

T = int(stdin.readline())

while T > 0:
    expr = stdin.readline()

    if '+' in expr:
        opr = '+'
        x, y = expr.split('+')
    elif '-' in expr:
        opr = '-'
        x, y = expr.split('-')
    else:
        opr = '*'
        x, y = expr.split('*')

    x = x.strip()
    y = y.strip()
    penAndPaperCalculation(x, y, opr)
    stdout.write('\n')
    T -= 1
