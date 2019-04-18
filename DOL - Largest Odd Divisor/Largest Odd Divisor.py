# Project name : SPOJ: DOL - Largest Odd Divisor
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-13
# Description  :
# Status       : Accepted (23629799)
# Tags         : python, largest odd divisor
# Comment      :

T = int(raw_input())

for t in xrange(T):
    n = int(raw_input())

    while n & 1 == 0:
        n = n >> 1

    print "Case " + str(t + 1) + ": " + str(n)
