# Project name : SPOJ: MOZSAO - Sharmeen and One
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-22
# Description  :
# Status       : Accepted (23669247)
# Tags         : python
# Comment      :

T = int(input())

while T > 0:
    n = int(input())

    print(' '.join(['one']*n) + '!'*n)
    T -= 1
