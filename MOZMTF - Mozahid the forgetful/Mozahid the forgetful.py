# Project name : SPOJ: MOZMTF - Mozahid the forgetful
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-22
# Description  :
# Status       : Accepted (23670146)
# Tags         : python
# Comment      :

n = input()
A = list(map(int, n))
s = int(input()) - sum(A)

res = ''
for i in range(10):
    if s <= A[i]:
        res += n[i]
    else:
        res += str(s) + n[i:]
        break
else:
    res += str(s)

print(res)
