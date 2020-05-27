# Project name : SPOJ: CHI_LOG - The real logarithm
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-21
# Description  :
# Status       : Accepted (23668073)
# Tags         : python, bignum arithmetic
# Comment      :

from decimal import *

getcontext().prec = 102

T = int(raw_input())

while T > 0:
    n = Decimal(raw_input())
    if n == Decimal('1'):
    	print '0'
    else:
    	print str(n.ln()).strip("0").replace(".", "")
    T -= 1
