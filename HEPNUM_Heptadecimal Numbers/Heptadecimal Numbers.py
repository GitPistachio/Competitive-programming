# Project name : SPOJ: HEPNUM - Heptadecimal Numbers
# Author       : Wojciech Raszka
# Date created : 2019-02-14
# Description  :
# Status       : Accepted (23233008)
# Comment      : 

a, b = input().split()

while a != '*':
    a, b = a.zfill(len(b)), b.zfill(len(a))

    if a < b:
        print('<')
    elif a > b:
        print('>')
    else:
        print('=')

    a, b = input().split()
