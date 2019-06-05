# Project name : SPOJ: DELEVE - Somma i numeri dispari
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-27
# Description  :
# Status       : Accepted (23506306)
# Tags         : python
# Comment      :

A = eval(input())

print(sum(map(lambda x: x if x % 2 else 0, A)))
