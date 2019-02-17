# Project name : SPOJ: NSYSTEM - Numeral System
# Author       : Wojciech Raszka
# Date created : 2019-02-13
# Description  :
# Status       : Accepted (23225203)
# Comment      :

def preffix(n, l):
    if n != '1':
        return n + l
    else:
        return l

def convert(n):
    mcxi = ''
    n = str(n)[::-1]
    if n[0] != '0':
        mcxi = preffix(n[0], "i")
    if len(n) > 1 and  n[1] != '0':
        mcxi = preffix(n[1], "x") + mcxi
    if len(n) > 2 and  n[2] != '0':
        mcxi = preffix(n[2], "c") + mcxi
    if len(n) > 3 and  n[3] != '0':
        mcxi = preffix(n[3], "m") + mcxi

    return mcxi

def deconvert(mcxi):
    preffix = 1
    n = 0
    for l in mcxi:
        if l == "m":
            n += 1000*preffix
            preffix = 1
        elif l == "c":
            n += 100*preffix
            preffix = 1
        elif l == "x":
            n += 10*preffix
            preffix = 1
        elif l == "i":
            n += preffix
            preffix = 1
        else:
            preffix = int(l)
    return n


n = int(input())

for i in range(n):
    a, b = input().split()
    print(convert(deconvert(a) + deconvert(b)))
