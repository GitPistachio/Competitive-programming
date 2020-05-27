# Project name : SPOJ: ANARC09B - Tiles of Tetris, Not!
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-11
# Description  :
# Status       : Accepted (23619376)
# Tags         : python, geometry, GCD, greatest common divisor
# Comment      :

def gcd(a, b):
  if b == 0:
    return a

  return gcd(b, a % b)

while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break

  if a == b:
    print(1)
  else:
    r = gcd(a, b)
    print(a*b//(r*r))
