# Project name : SPOJ: INTEST - Enormous Input Test
# Author       : Wojciech Raszka
# Date created : 2019-03-15
# Description  :
# Status       : Accepted (23420289)
# Comment      :

from sys import stdin, stdout

n, k = map(int, stdin.readline().split())

stdout.write(str(sum(map(lambda x: 1 if int(x) % k == 0 else 0 , stdin))))
