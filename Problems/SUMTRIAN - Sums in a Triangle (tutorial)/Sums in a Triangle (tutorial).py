# Project name : SPOJ: SUMTRIAN - Sums in a Triangle (tutorial)
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-21
# Description  :
# Status       : Accepted (23955438)
# Tags         : python, dynamic-programming
# Comment      :

T = int(raw_input())
while T > 0:
  n = int(raw_input())
  P = [0]*(n + 1)

  for i in range(n):
    row = [int(val) for val in raw_input().split()]
    x = 0
    for j in range(i + 1):
      P[j + 1], x = row[j] + max(x, P[j + 1]), P[j + 1]

  print max(P)

  T-=1
