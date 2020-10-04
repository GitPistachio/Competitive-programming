# Project name : HackerRank: Sorting Bubble Sort
# Link         : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-18
# Description  :
# Status       : Accepted (169506933)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
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

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
