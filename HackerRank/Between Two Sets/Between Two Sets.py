# Project name : HackerRank: Between Two Sets
# Link         : https://www.hackerrank.com/challenges/between-two-sets/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-28
# Description  :
# Status       : Accepted (166121538)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)

    total_x = 0
    for x in range(max_a, min_b + 1, max_a):
        is_between = True
        for val in a:
            if x % val != 0:
                is_between = False
                break
        
        if is_between:
            for val in b:
                if val % x != 0:
                    is_between = False
                    break
        
        if is_between:
            total_x += 1
        
    return total_x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
