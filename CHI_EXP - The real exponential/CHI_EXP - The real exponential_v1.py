# Project name : SPOJ: CHI_EXP - The real exponential
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-14
# Description  :
# Status       : Accepted (24863973)
# Tags         : python, bignum arithmetic, MacLaurin series of exponential funcion
# Comment      : 10 points. The formula is exp(x) = 1 + x + x^2/2! + x^3/3! + ...

from sys import stdin, stdout
from decimal import *
import re
getcontext().prec = 2000

def exp(x):
  a = Decimal(1)
  b = Decimal(1)
  res = a/b

  i = 1
  while i < 520:
    a *= x
    b *= i
    res += a/b
    i += 1

  return res

def normalize(x):
  x = str(x.normalize()).replace('.', '')
  x = re.sub(r'^0+', '', x)
  x = x[:101]
  x = re.sub(r'0+$', '', x)

  return x if x != '' else 0


T = int(stdin.readline())

while T > 0:
  x = Decimal(stdin.readline())
  y = exp(x)

  stdout.write(normalize(y)  + '\n')

  T -= 1
