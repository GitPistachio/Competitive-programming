# Project name : SPOJ: The ball game
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-02-12
# Description  :
# Status       : Accepted (23218850)
# Tags         : python, math, probability theory, combinatorics
# Comment      : The max probability is when N-1 boxes have exacly one white ball and non black balls. The rest of balls is in the last box.

T = int(input())

for t in range(T):
  N = int(input())
  p = round(((N - 1) + 1/(N + 1))/N, 8)
  print("{:.8f}".format(p))
