# Project name : SPOJ: NODESC1 - No Description 1
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-02
# Description  :
# Status       : Accepted (23555290)
# Tags         : python, fibonacci, brute force
# Comment      : Solution: for n print F(n) chars '?', where F(n) is a fibonacci sequence

def F(n):
	if n > 1:
		return F(n - 1) + F(n - 2)
	elif n == 1:
		return 1
	else:
		return 0

n = int(input())
print("?"*F(n))
