# Project name : SPOJ: CHI_SIN - The real sine
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-17
# Description  :
# Status       : Accepted (24885994)
# Tags         : python, bignum arithmetic, MacLaurine expansion of sin(x).
# Comment      : 10 points, The formula is sin(x) = x - x^3/3! + x^5/5! - ...

from sys import stdin, stdout
from decimal import *
import re
getcontext().prec = 150

def sin(x):
  a = x
  b = Decimal(1)
  res = a/b

  i = 1
  while i < 100:
    a *= -x*x
    b *= 2*i*(2*i + 1)
    res += a/b
    i += 1

  return res

def normalize(x):
  x = str(x.normalize()).replace('.', '')
  x = re.sub(r'^0+', '', x)
  x = x[:102]
  x = re.sub(r'0+$', '', x)

  return x if x != '' else '0'


T = int(stdin.readline())

while T > 0:
  x = Decimal(stdin.readline())
  y = sin(x)

  stdout.write(normalize(y)  + '\n')

  T -= 1
