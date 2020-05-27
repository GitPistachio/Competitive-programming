# Project name : SPOJ: STRHH - Half of the half
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23290176)
# Comment      :

T = int(input())

for t in range(T):
    l = input()
    print(l[:len(l)//2:2])
