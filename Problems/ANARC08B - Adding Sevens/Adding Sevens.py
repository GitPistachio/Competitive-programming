# Project name : SPOJ: ANARC08B - Adding Sevens
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-11
# Description  :
# Status       : Accepted (23619944)
# Tags         : python, a seven segment display
# Comment      :

import textwrap

def codeToDigit(code):
    if code == '063':
        return 0
    elif code == '010':
        return 1
    elif code == '093':
        return 2
    elif code == '079':
        return 3
    elif code == '106':
        return 4
    elif code == '103':
        return 5
    elif code == '119':
        return 6
    elif code == '011':
        return 7
    elif code == '127':
        return 8
    elif code == '107':
        return 9
    else:
        return 0

def digitToCode(d):
    if d == 0:
        return '063'
    elif d == 1:
        return '010'
    elif d == 2:
        return '093'
    elif d == 3:
        return '079'
    elif d == 4:
        return '106'
    elif d == 5:
        return '103'
    elif d == 6:
        return '119'
    elif d == 7:
        return '011'
    elif d == 8:
        return '127'
    elif d == 9:
        return '107'


def decode(A):
    a = 0
    for code in textwrap.wrap(A, 3):
        a = a*10 + codeToDigit(code)

    return a

def encode(a):
    return ''.join(map(lambda x: digitToCode(int(x)), str(a)))

while True:
    entry = input()
    if entry == 'BYE':
        break

    A, B = entry.replace("=", "").split("+")

    c = decode(A) + decode(B)

    print(entry, encode(c), sep='')
