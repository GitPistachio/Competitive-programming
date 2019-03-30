# Project name : SPOJ: CRS - Crying Series
# Author       : Wojciech Raszka
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23531393)
# Tags         : python
# Comment      : 65 chars

def p(x):
	x = int(input())
	return x*(x > 0)

print(sum(map(p, range(p(1)))))
