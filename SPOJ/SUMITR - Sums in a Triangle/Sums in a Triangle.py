# Project name : SPOJ: SUMITR - Sums in a Triangle
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-21
# Description  :
# Status       : Accepted (23592215)
# Tags         : python, dynamic-programming
# Comment      :

def r():
  return list(map(int,raw_input().split()))
T=r()[0]
while T>0:
  n=r()[0];P=[0]*100
  for i in range(n):
    C=r();x=0
    for j in range(1,i+2):
      P[j],x=C[j-1]+max(x,P[j]),P[j]
  print max(P)
  T-=1
