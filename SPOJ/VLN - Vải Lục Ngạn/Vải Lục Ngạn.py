# Project name : SPOJ: VLN - Vải Lục Ngạn
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-11-08
# Description  :
# Status       : Accepted (24807755)
# Tags         : python, sliding window technique
# Comment      : 100 score

from sys import stdin, stdout

n, h = map(int, stdin.readline().split())
A = [int(x) for x in stdin.readline().split()]

no_of_harvest_side_trees = h//3
max_no_of_picked_fruits = 0
i = 0

while i <= no_of_harvest_side_trees:
  max_no_of_picked_fruits += A[i]
  i += 1

no_of_picked_fruits = max_no_of_picked_fruits
for i in range(no_of_harvest_side_trees + 1, n):
  no_of_picked_fruits += A[i]

  if i > (no_of_harvest_side_trees << 1):
    no_of_picked_fruits -= A[i - (no_of_harvest_side_trees << 1) - 1]

  if no_of_picked_fruits > max_no_of_picked_fruits:
    max_no_of_picked_fruits = no_of_picked_fruits

stdout.write('%s\n' % max_no_of_picked_fruits)
