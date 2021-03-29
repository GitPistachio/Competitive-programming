# Project name : SPOJ: MAJOR - Majority
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-11-07
# Description  :
# Status       : Accepted (24800390)
# Tags         : python, sliding window technique
# Comment      :

from sys import stdin, stdout


T = int(stdin.readline())
MAX_A = 1000

while T > 0:
  n = int(stdin.readline())
  if n == 0:
  	stdout.write('NO\n')
  	T -= 1
  	continue
  C = [0]*((MAX_A << 1) + 1)
  max_occ_a = None
  for a in map(int, stdin.readline().split()):
  	C[MAX_A + a] += 1
  	if C[MAX_A + a] << 1 > n:
  		max_occ_a = a
  		break
  if max_occ_a is None:
  	stdout.write('NO\n')
  else:
  	stdout.write('YES %s\n' % max_occ_a)

  T -= 1
