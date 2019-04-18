# Project name : SPOJ: AVG - AVERAGE
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-14
# Description  :
# Status       : Accepted (23634195)
# Tags         : python, math, average
# Comment      :

T = int(raw_input())

while T > 0:
	n = int(raw_input())
	print sum(map(int, raw_input().split()))/n
	T -= 1
