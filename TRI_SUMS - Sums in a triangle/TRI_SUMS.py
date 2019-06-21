# Project name : SPOJ: TRI_SUMS - Sums in a triangle
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-21
# Description  :
# Status       : Accepted (23955188)
# Tags         : python, dynamic-programming
# Comment      : 209

def r():return list(map(int,raw_input().split()))
T=r()[0]
while T>0:
  n=r()[0];P=[0]*101;T-=1
  for i in range(n):
    C=r();x=0
    for j in range(1,i+2):
      P[j],x=C[j-1]+max(x,P[j]),P[j]
  print max(P)
