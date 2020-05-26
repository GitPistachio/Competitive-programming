# Project name : SPOJ: CHI_EXP - The real exponential
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-17
# Description  :
# Status       : Accepted (24885907)
# Tags         : python, bignum arithmetic
# Comment      : 10 points

from decimal import *
import re

getcontext().prec = 102

def normalize(x):
  x = str(x.normalize()).replace('.', '')
  x = re.sub(r'^0+', '', x)
  x = x[:101]
  x = re.sub(r'0+$', '', x)

  return x if x != '' else 0

T = int(raw_input())

while T > 0:
    n = Decimal(raw_input())
    if n == Decimal('0'):
    	print '1'
    else:
    	print normalize(n.exp())
    T -= 1
