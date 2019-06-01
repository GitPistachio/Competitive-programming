# Project name : SPOJ: ADDREV -  Adding Reversed Numbers
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-??-??
# Description  :
# Status       : Accepted ()
# Tags         : python
# Comment      :

no_of_cases = int(input())

for c in range(no_of_cases):
    print(int(str(sum(map(lambda s: int(s[::-1]), input().split(' '))))[::-1]))
