# Project name : SPOJ: MUL - Fast Multiplication
# Author       : Wojciech Raszka
# E-mail       : gitpistachi@gmail.com
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23373544)
# Tags         : python
# Comment      :

T = int(input())

for t in range(T):
    l1, l2 = map(int, input().split())
    print(l1*l2)
