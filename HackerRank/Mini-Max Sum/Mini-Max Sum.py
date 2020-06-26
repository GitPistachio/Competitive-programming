# Project name : HackerRank: Mini-Max Sum
# Link         : https://www.hackerrank.com/challenges/mini-max-sum/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-22
# Description  :
# Status       : Accepted (165271743)
# Tags         : python, console patters, staircase
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_a = min(arr)
    max_a = max(arr)

    total = sum(arr)

    print('{} {}'.format(total - max_a, total - min_a))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
