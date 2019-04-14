# Project name : SPOJ: ANARC08E - Relax! It is just a game
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-14
# Description  :
# Status       : Accepted (23633884)
# Tags         : python, math, combinatorics
# Comment      :

while True:
	a, b = map(int, input().split())
	if a == -1 or b == -1:
		break
	elif a + b - 1 == a or 1 == a:
		print(a, "+", b, "=", a + b, sep="")
	else:
		print(a, "+", b, "!=", a + b, sep="")
