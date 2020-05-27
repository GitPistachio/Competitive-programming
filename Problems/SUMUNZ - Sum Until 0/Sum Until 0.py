# Project name : SPOJ: SUMUNZ - Sum Until 0
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483801)
# Tags         : python
# Comment      :

A = eval(input())
try:
    idx = A.index(0)
except:
    idx = -1

if idx != -1:
    print(sum(A[:idx]))
else:
    print(sum(A))
