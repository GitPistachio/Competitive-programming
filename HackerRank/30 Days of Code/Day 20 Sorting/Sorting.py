# Project name : HackerRank: Day 20: Sorting
# Link         : https://www.hackerrank.com/challenges/30-sorting/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-10
# Description  :
# Status       : Accepted (168241466)
# Tags         : python, optimized bubble sort algorithm
# Comment      : 

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

no_of_swaps = 0
for i in range(n):
    swap = False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            no_of_swaps += 1
            swap = True
    
    if not swap:
        break

print('Array is sorted in {} swaps.'.format(no_of_swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))