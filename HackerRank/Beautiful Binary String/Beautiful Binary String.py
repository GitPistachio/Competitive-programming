# Project name : HackerRank: Beautiful Binary String
# Link         : https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-15
# Description  :
# Status       : Accepted (208928621)
# Tags         : python
# Comment      : for fragments 01010 it is enough to change middle 0 to 1. 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    x = y = None
    k = 0
    for d in b:
        if x == '0' and y == '1' and d == '0':
            k += 1
            x, y = '1', '1'
        else:
            x, y = y, d
    return k
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

