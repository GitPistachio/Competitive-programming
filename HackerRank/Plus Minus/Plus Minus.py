# Project name : HackerRank: Plus Minus
# Link         : https://www.hackerrank.com/challenges/plus-minus/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-22
# Description  :
# Status       : Accepted (165253015)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    freq = {-1: 0, 0: 0, 1:0}
    for a in arr:
        freq[sign(a)] += 1
    
    for i in [1, -1, 0]:
        print('{:.6f}'.format(freq[i]/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
