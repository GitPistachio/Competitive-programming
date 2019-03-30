# Project name : SPOJ: S1P4 - Celebration
# Author       : Wojciech Raszka
# Date created : 2019-03-25
# Description  :
# Status       : Accepted (23489619)
# Tags         : python
# Comment      :

tokens = raw_input().split()
x = int(float(tokens[0]))
A = x*7
B = int(tokens[1])*int(tokens[1])

if (x + 1) % 2 == 0 and (A + B) <= 100:
	print 1
else:
	print 0
