# Project name : SPOJ: ARRANGE - Arranging Amplifiers
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-20
# Description  :
# Status       : Accepted (24907533)
# Tags         : python
# Comment      : Inq. 1

from sys import stdin, stdout

T = int(stdin.readline())

while T > 0:
	n = int(stdin.readline())
	A = [int(x) for x in stdin.readline().split()]
	A.sort(reverse=True)
	if len(A) >= 2 and A[0] == 3 and A[1] == 2:
		A[0] = 2
		A[1] = 3

	try:
		idx_1 = A.index(1)
		A = A[idx_1:] + A[:idx_1]
	except:
		pass

	stdout.write(' '.join([str(a) for a in A]) + '\n')
	T -= 1
