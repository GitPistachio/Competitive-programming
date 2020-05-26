# Project name : SPOJ: SCP11B Alaska
# Author       : Wojciech Raszka
# Date created : 2019-02-13
# Description  :
# Status       : Accepted (23225055)
# Comment      :

n = int(input())

while n > 0:
	stations = [int(input()) for i in range(n)]

	if stations is None:
		print("IMPOSSIBLE")
	else:
		stations.sort()

		is_possible = True
		if stations[0] > 200:
			is_possible = False
		else:
			for i in range(1, n):
			    if stations[i] - stations[i - 1] > 200:
			        is_possible= False
			        break
			else:
			    if (1422 - stations[n - 1])*2 > 200:
			    	is_possible = False

		if is_possible:
			print("POSSIBLE")
		else:
			print("IMPOSSIBLE")

	n = int(input())
